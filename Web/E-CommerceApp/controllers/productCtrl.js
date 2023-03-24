const Product = require("../models/Product");
const asyncHandler = require("express-async-handler");
const slugify = require("slugify");

// 상품 등록
const createProduct = asyncHandler(async (req, res) => {
  try {
    if (req.body.title) {
      // slugify : 텍스트를 url 주소로 변환해주는 라이브러리
      // slug : 이미 얻은 데이터를 사용하여 유효한 URL을 생성 (URL과 의미있는 이름을 사용)
      req.body.slug = slugify(req.body.title);
    }
    const newProduct = await Product.create(req.body);
    res.json(newProduct);
  } catch (error) {
    throw new Error(error);
  }
});

// 상품 수정
const updateProduct = asyncHandler(async (req, res) => {
  const { id } = req.params;
  try {
    if (req.body.title) {
      // slugify : 텍스트를 url 주소로 변환해주는 라이브러리
      // slug : 이미 얻은 데이터를 사용하여 유효한 URL을 생성 (URL과 의미있는 이름을 사용)
      req.body.slug = slugify(req.body.title);
    }
    const updateProduct = await Product.findOneAndUpdate(id,
      req.body, {
      new: true,
    });
    res.json(updateProduct);
  } catch (error) {
    throw new Error(error);
  }
});

// 상품 삭제
const deleteProduct = asyncHandler(async (req, res) => {
  const { id } = req.params;
  try {
    if (req.body.title) {
      // slugify : 텍스트를 url 주소로 변환해주는 라이브러리
      // slug : 이미 얻은 데이터를 사용하여 유효한 URL을 생성 (URL과 의미있는 이름을 사용)
      req.body.slug = slugify(req.body.title);
    }
    const deleteProduct = await Product.findOneAndDelete(id);
    res.json(deleteProduct);
  } catch (error) {
    throw new Error(error);
  }
});

// 상품 id 조회
const getAProduct = asyncHandler(async (req, res) => {
  const { id } = req.params;
  try {
    const findProduct = await Product.findById(id);
    res.json(findProduct);
  } catch (error) {
    throw new Error(error);
  }
});

// 모든 상품 조회
const getAllProduct = asyncHandler(async (req, res) => {
  try {
    // 1) Filtering => t?price[lt]=50000
    const queryObj = { ...req.query };
    const excludeFields = ["page", "sort", "limit", "fields"];
    excludeFields.forEach((el) => delete queryObj[el])
    console.log(queryObj);

    // JSON.stringify : JavaScript 값이나 객체를 JSON 문자열로 변환
    let queryStr = JSON.stringify(queryObj);
    // Create operators ($gt, $gte, etc)
    queryStr = queryStr.replace(/\b(gt|gte|lt|lte)\b/g, (match) => `$${match}`);
    // JSON.parse : JSON 문자열을 인자로 받고 결과값으로 JavaScript 객체를 반환
    let query = Product.find(JSON.parse(queryStr));

    // 2)Sorting => ?sort=-category,-brand
    if (req.query.sort) {
      const sortBy = req.query.sort.split(",").join(" ");
      query = query.sort(sortBy);
    } else {
      query = query.sort("-createdAt");
    }

    // 3) Limiting the fields => ?fields=-title,-price,-category
    if (req.query.fields) {
      const fields = req.query.fields.split(",").join(" ");
      query = query.select(fields);
    } else {
      query = query.select("-__v");
    }

    // 4) pagination  => ?page=4&limit=5
    // 페이지 나누기, 쿼리의 결과값으로 리턴된 리소스를 분할하여 전달
    const page = req.query.page;
    const limit = req.query.limit;
    const skip = (page - 1) * limit;
    query = query.skip(skip).limit(limit);
    if (req.query.page) {
      const productCount = await Product.countDocuments();
      if (skip >= productCount) {
        throw new Error("This page does not exists");
      }
    }
    // console.log(page, limit, skip);

    const product = await query;
    res.json(product);
  } catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createProduct,
  updateProduct,
  deleteProduct,
  getAProduct,
  getAllProduct
};