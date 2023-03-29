const Blog = require("../models/Blogs");
const User = require("../models/User");
const asyncHandler = require("express-async-handler");
const { validateMongodbID } = require("../utils/validateMongodbID");

const createBlog = asyncHandler(async (req, res) => {
  try {
    const newBlog = await Blog.create(req.body);
    res.json({
      status: "success",
      newBlog,
    });
  }
  catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createBlog
}