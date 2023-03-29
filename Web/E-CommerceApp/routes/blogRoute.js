const express = require("express");
const { createBlog, updateBlog, getBlog } = require("../controllers/blogCtrl");
const { authMiddleware, isAdmin } = require("../middlewares/authMiddleware");
const router = express.Router();

router.post("/", authMiddleware, isAdmin, createBlog);
router.put("/:id", updateBlog);
router.get("/:id", getBlog);

module.exports = router;