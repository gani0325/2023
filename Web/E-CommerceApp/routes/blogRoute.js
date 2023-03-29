const express = require("express");
const { createBlog, updateBlog, getBlog, getAllBlogs } = require("../controllers/blogCtrl");
const { authMiddleware, isAdmin } = require("../middlewares/authMiddleware");
const router = express.Router();

router.post("/", authMiddleware, isAdmin, createBlog);
router.put("/:id", updateBlog);
router.get("/:id", getBlog);
router.get("/", getAllBlogs);

module.exports = router;