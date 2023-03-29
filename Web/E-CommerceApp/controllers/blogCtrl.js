const Blog = require("../models/Blogs");
const User = require("../models/User");
const asyncHandler = require("express-async-handler");
const { validateMongodbID } = require("../utils/validateMongodbID");

// 블로그 생성하기
const createBlog = asyncHandler(async (req, res) => {
  try {
    const newBlog = await Blog.create(req.body);
    res.json(newBlog);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 블로그 수정하기
const updateBlog = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const updateBlog = await Blog.findByIdAndUpdate(id, req.body);
    res.json(updateBlog);
  }
  catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createBlog,
  updateBlog,

}