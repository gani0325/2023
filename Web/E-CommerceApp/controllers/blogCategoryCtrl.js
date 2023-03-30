const blogCategorySchema = require("../models/BlogCategory");
const asyncHandler = require("express-async-handler");
const { validateMongodbID } = require("../utils/validateMongodbID");

// 블로그 생성하기
const createCategory = asyncHandler(async (req, res) => {
  try {
    const newCategory = await blogCategorySchema.create(req.body);
    res.json(newCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 블로그 수정하기
const updateCategory = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const updateCategory = await blogCategorySchema.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    res.json(updateCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 블로그 삭제하기
const deleteCategory = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const deleteCategory = await blogCategorySchema.findByIdAndDelete(id);
    res.json(deleteCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 블로그 조회하기
const getaCategory = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const getaCategory = await blogCategorySchema.findById(id);
    res.json(getaCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 모든 블로그 조회하기
const getallCategory = asyncHandler(async (req, res) => {
  try {
    const getallCategory = await blogCategorySchema.find();
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