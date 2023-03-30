const Category = require("../models/Category");
const asyncHandler = require("express-async-handler");
const validateMongodbID = require("../utils/validateMongodbID");

// 카테고리 생성하기
const createCategory = asyncHandler(async (req, res) => {
  try {
    const newCategory = await Category.create(req.body);
    res.json(newCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 카테고리 수정하기
const updateCategory = asyncHandler(async (req, res) => {
  const { id } = req.params;
  try {
    const updateCategory = await Category.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    res.json(updateCategory);
  }
  catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createCategory,
  updateCategory,

}