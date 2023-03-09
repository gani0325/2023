const express = require("express");
const router = express.Router();
const User = require("../models/user");
const multer = require("multer");

// image upload
var storage = multer.diskStorage({
  // 파일이 업로드될 경로 설정
  destination: function (req, file, cb) {
    cb(null, "./uploads");
  },
  // timestamp를 이용해 새로운 파일명 설정
  filename: function (req, file, cb) {
    cb(null, file.fieldname + "_" + Date.now() + "_" + file.originalname);
  }
})

var upload = multer({
  storage: storage,
}).single("image");   // 한 개의 이미지 처리

// Insert an user into database route
router.post("/add", upload, (req, res) => {
  const user = new User({
    name: req.body.name,
    email: req.body.email,
    phone: req.body.phone,
    image: req.file.filename,
  });

  user.save().then((err) => {
    // index.js 에 res.locals.message 있음
    req.session.message = {
      type: "success",
      message: "User added successsfull!"
    };
    // 지정된 다른 URL로 재요청 (홈)
    res.redirect("/");
  }).catch((err) => {
    res.json({ message: err.message, type: "danger" });
  })
});

// Home (ejs 와 연동)
router.get("/", (req, res) => {
  res.render("index", { title: "Home" });
});

router.get("/add", (req, res) => {
  res.render("addUsers", { title: "Add users" });
})

module.exports = router;