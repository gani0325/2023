const prodCategorySchema = require("../models/ProdCategory");
const asyncHandler = require("express-async-handler");
const { validateMongodbID } = require("../utils/validateMongodbID");

// 상품 카테고리 생성하기
const createCategory = asyncHandler(async (req, res) => {
  try {
    const newCategory = await prodCategorySchema.create(req.body);
    res.json(newCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 상품 카테고리 수정하기
const updateCategory = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const updateCategory = await prodCategorySchema.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    res.json(updateCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 상품 카테고리 삭제하기
const deleteCategory = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const deleteCategory = await prodCategorySchema.findByIdAndDelete(id);
    res.json(deleteCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 상품 카테고리 조회하기
const getaCategory = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const getaCategory = await prodCategorySchema.findById(id);
    res.json(getaCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 모든 상품 카테고리 조회하기
const getallCategory = asyncHandler(async (req, res) => {
  try {
    const getallCategory = await prodCategorySchema.find();
    res.json(getallCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createCategory,
  updateCategory,
  deleteCategory,
  getaCategory,
  getallCategory,

}