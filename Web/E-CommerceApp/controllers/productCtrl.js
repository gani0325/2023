const Product = require("../models/Product");
const User = require("../models/User");
const asyncHandler = require("express-async-handler");
const slugify = require("slugify");
const { validateMongodbID } = require("../utils/validateMongodbID");
const cloudinaryUploadImg = require("../utils/cloudinary");

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
  validateMongodbID(id);
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
  validateMongodbID(id);
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
  validateMongodbID(id);

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

// 위시리스트에 상품 넣기
const addTowishList = asyncHandler(async (req, res) => {
  const { _id } = req.user;
  const { prodId } = req.body;
  try {
    const user = await User.findById(_id);
    const alreadyadded = user.wishList.find((id) => id.toString() === prodId);

    if (alreadyadded) {
      let user = await User.findByIdAndUpdate(_id, {
        $pull: { wishList: prodId },
      }, {
        new: true,
      });
      res.json(user);
    } else {
      let user = await User.findByIdAndUpdate(_id, {
        $push: { wishList: prodId },
      }, {
        new: true,
      });
      res.json(user);
    }
  } catch (error) {
    throw new Error(error);
  }
});

// 상품 별점 매기기
const rating = asyncHandler(async (req, res) => {
  const { _id } = req.user;
  const { star, comment, prodId } = req.body;

  try {
    const product = await Product.findById(prodId);
    let alreadyRated = product.ratings.find(
      (userId) => userId.toString() === _id.toString());

    if (alreadyRated) {
      const updateRating = await Product.updateOne(
        {
          ratings: { $elemMatch: alreadyRated },
        }, {
        $set: { "ratings.$.star": star, "ratings.$.comment": comment },
      }, {
        new: true
      });
      // res.json(updateRating);
    } else {
      const rateProduct = await Product.findByIdAndUpdate(
        prodId,
        {
          $push: {
            ratings: {
              star: star,
              comment: comment,
              postedby: _id,
            },
          },
        });
      // res.json(rateProduct);
    }

    // 총 별점 평균내기
    const getallratings = await Product.findById(prodId);
    let totalRating = getallratings.ratings.length;   // 개수
    let ratingsum = getallratings.ratings
      .map((item) => item.star)
      .reduce((prev, curr) => prev + curr, 0);
    let actualRating = Math.round(ratingsum / totalRating);
    let finalproduct = await Product.findByIdAndUpdate(
      prodId, {
      totalrating: actualRating,
    }, {
      new: true
    });
    res.json(finalproduct);
  } catch (error) {
    throw new Error(error);
  }
});

const uploadImages = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const uploader = (path) => cloudinaryUploadImg(path, "images");
    const urls = [];
    const files = req.files;
    for (const file of files) {
      const { path } = files;
      const newpath = await uploader(path);
      urlspush(newpath);
    }
    const findProduct = await Product.findByIdAndUpdate(
      id,
      {
        images: urls.map((file) => {
          return file;
        }),
      },
      {
        new: true,
      }
    );
    res.json(findProduct);
  } catch (error) {
    throw new Error(error);
  }

});

module.exports = {
  createProduct,
  updateProduct,
  deleteProduct,
  getAProduct,
  getAllProduct,
  addTowishList,
  rating,
  uploadImages
};