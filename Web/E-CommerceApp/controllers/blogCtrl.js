const Blog = require("../models/Blog");
const User = require("../models/User");
const asyncHandler = require("express-async-handler");
const { validateMongodbID } = require("../utils/validateMongodbID");
const cloudinaryUploadImg = require("../utils/cloudinary");
const fs = require("fs");

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
    const getBlog = await Blog.findById(id)
    .populate("likes")
    .populate("dislikes");
    const updateViews = await Blog.findByIdAndUpdate(
      id,
      {
        $inc: { numViews: 1 },    // 조회할 때마다 numViews 올라감~
      },
      { new: true }
    );
    res.json(getBlog);
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

// 좋아하는 블로그 저장
const likeBlog = asyncHandler(async (req, res) => {
  const { blogId } = req.body;
  validateMongodbID(blogId);

  // find the blog which you want to be liked
  const blog = await Blog.findById(blogId);
  // find the login user
  const loginUserId = req?.user?._id;
  // find if the user has liked the post
  const isLiked = blog?.isLiked;

  // find if the user has disliked the blog
  const alreadyDisLiked = blog?.dislikes?.find(
    (userId) => userId?.toString() === loginUserId?.toString());

  if (alreadyDisLiked) {
    const blog = await Blog.findByIdAndUpdate(blogId, {
      $pull: { dislikes: loginUserId },
      isDisliked: false,
    },
      { new: true });
    res.json(blog);
  }

  // 좋아하면 (true) -> 아닌걸로 (false)
  if (isLiked) {
    const blog = await Blog.findByIdAndUpdate(blogId, {
      $pull: { likes: loginUserId },
      isLiked: false,
    },
      { new: true });
    res.json(blog);
  }
  // 아니었는데 (false) -> 좋아하는걸로 (true)
  else {
    const blog = await Blog.findByIdAndUpdate(blogId, {
      $push: { likes: loginUserId },
      isLiked: true,
    },
      { new: true });
    res.json(blog);
  }
});

// 싫어하는 블로그 저장
const dislikeBlog = asyncHandler(async (req, res) => {
  const { blogId } = req.body;
  validateMongodbID(blogId);

  // find the blog which you want to be liked
  const blog = await Blog.findById(blogId);
  // find the login user
  const loginUserId = req?.user?._id;
  // find if the user has disliked the post
  const isDisLiked = blog?.isDisliked;

  // find if the user has disliked the blog
  const alreadyLiked = blog?.likes?.find(
    (userId) => userId?.toString() === loginUserId?.toString());

  if (alreadyLiked) {
    const blog = await Blog.findByIdAndUpdate(blogId, {
      $pull: { likes: loginUserId },
      isLiked: false,
    },
      { new: true });
    res.json(blog);
  }

  // 싫어하면 (true) -> 아니었던걸로 (false)
  if (isDisLiked) {
    const blog = await Blog.findByIdAndUpdate(blogId, {
      $pull: { dislikes: loginUserId },
      isDisliked: false,
    },
      { new: true });
    res.json(blog);
  }
  // 아니었는면 (false) -> 싫어하는걸로 (true)
  else {
    const blog = await Blog.findByIdAndUpdate(blogId, {
      $push: { dislikes: loginUserId },
      isDisliked: true,
    },
      { new: true });
    res.json(blog);
  }
});

// 블로그 이미지 업로드하기
const uploadImages = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const uploader = (path) => cloudinaryUploadImg(path, "images");
    const urls = [];
    const files = req.files;
    for (const file of files) {
      const { path } = file;
      const newpath = await uploader(path);
      urls.push(newpath);
      // unlinkSync 파일 삭제
      fs.unlinkSync(path);
    }
    const findBlog = await Blog.findByIdAndUpdate(
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
    res.json(findBlog);
  } catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createBlog,
  updateBlog,
  getBlog,
  getAllBlogs,
  deleteBlog,
  likeBlog,
  dislikeBlog,
  uploadImages

}