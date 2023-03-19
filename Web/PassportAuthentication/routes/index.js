const express = require("express");
const router = express.Router();
const { ensureAuthenticated } = require("../middlewares/auth");

// Main page
router.get("/", (req, res) => {
  // rednering 할 때 view의 파일 이름 써야됨
  res.render("welcome");
});

// dashboard
router.get("/dashboard", ensureAuthenticated, (req, res) => {
  // rendering 할 때 view의 파일 이름 써야됨
  res.render("dashboard", {
    name : req.user.name
  });
});

module.exports = router;