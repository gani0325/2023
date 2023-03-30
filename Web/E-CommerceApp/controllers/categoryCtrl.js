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

module.exports = {
  createCategory,
}