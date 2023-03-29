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

// 블로그 조회하기
const getBlog = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const getBlog = await Blog.findById(id);
    const updateViews = await Blog.findByIdAndUpdate(
      id,
      {
        $inc: { numViews: 1 },    // 조회할 때마다 numViews 올라감~
      },
      { new: true }
    );
    res.json(updateViews);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 모든 블로그 조회하기
const getAllBlogs = asyncHandler(async (req, res) => {
  try {
    const getAllBlogs = await Blog.find();
    res.json(getAllBlogs);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 블로그 삭제하기
const deleteBlog = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const deleteBlog = await Blog.findByIdAndDelete(id);
    res.json(deleteBlog);
  }
  catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createBlog,
  updateBlog,
  getBlog,
  getAllBlogs,
  deleteBlog

}