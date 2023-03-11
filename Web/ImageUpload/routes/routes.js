const express = require("express");
const router = express.Router();
const User = require("../models/user");
const multer = require("multer");
const fs = require("fs");

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

// 1) Get all users route
router.get("/", async (req, res) => {
  const user = await User.find();

  try {
    // Query를 이용할 때 프로미스를 리턴받고 싶다면 exec() 메서드를 이용
    // find()를 실행하여 Query의 인스턴스를 리턴
      res.render("index", {
        title: "Home Page",
        // 궁금 : 너 왜 error 잡히니?
        users: user
      });
  } catch (error) {
    (error) => {
      res.json({ message: error.message });
    }
  };
});

router.get("/add", (req, res) => {
  res.render("addUsers", { title: "Add users" });
})

// 2) Edit an user routes
router.get("/edit/:id", async (req, res) => {
  let id = req.params.id;
  const user = await User.findById(id);

  try {
    if (user == null) {
      res.redirect("/");
    } else {
      res.render("editUsers", {
        title: "Edit User",
        user: user,
      });
    }
  } catch (err) {
    res.redirect("/");
  }
});

// 3) Update user route
router.post("/update/:id", upload , async (req, res) => {
  let id = req.params.id;
  let new_image = "";

  if (req.file) {
    new_image = req.file.filename;
    try {
      // 동기 방식으로 파일 정보 읽기
      fs.readFileSync("./uploads/" + req.body.old_image);
    } catch(err) {
      console.log(err);
    }
  } else {
    req.image = req.body.old_image;
  }
    
  //  첫 번째 인자는 업데이트 하고자 하는 문서의 id, 두 번째 인자는 업데이트 할 정보 혹은 내용
  const user = await User.findByIdAndUpdate(id, {
    name : req.body.name,
    email : req.body.email,
    phone : req.body.phone,
    image : new_image
  });
  
  try {
    req.session.message = {
      type : "success",
      message :"User updated successfully!",
    };
    res.redirect("/");
  } catch (err) {
    res.json({ message : err.message, type : "danger"});
  }
  
});

module.exports = router;