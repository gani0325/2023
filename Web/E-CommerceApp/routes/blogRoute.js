const express = require("express");
const { createBlog, updateBlog } = require("../controllers/blogCtrl");
const { authMiddleware, isAdmin } = require("../middlewares/authMiddleware");
const router = express.Router();

router.post("/", authMiddleware, isAdmin, createBlog);
router.put("/:id", updateBlog);

module.exports = router;