// 파일을 업로드 하기 위한 node.js 미들웨어
const multer = require("multer");
// 이미지를 처리하기 좋은 패키지
const sharp = require("sharp");
// 파일/폴더/디렉터리 등의 경로를 편리하게 설정할 수 있는 기능
const path = require("path");
const fs = require("fs");

// 이미지 저장소
const multerStorage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, path.join(__dirname, "../public/images"));
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + "-" + Math.fround(Math.random() * 1e9);
    cb(null, file.fieldname + "-" + uniqueSuffix + ".jpeg");
  },
});

const multerFilter = (req, file, cb) => {
  // mime type : 파일이 어떠한 종류의 파일인지에 대한 정보가 담긴 라벨
  if (file.mimetype.startsWith("image")) {
    // 반환받은 Mime Type에 대한 데이터가 image 인지 체크
    cb(null, true)
  }
  else {
    cb(
      {
        message: "Unsupported file format",
      },
      false
    );
  }
};

const uploadPhoto = multer({
  storage: multerStorage,
  fileFilter: multerFilter,
  limits: { fieldSize: 2000000 },
});

// 이미지 사이즈 조정
const productImgResize = async (req, res, next) => {
  if (!req.files) return next();
  await Promise.all(
    req.files.map(async (file) => {
      await sharp(file.path)
        .resize(300, 300)
        .toFormat("jpeg")
        .jpeg({ quality: 90 })
        .toFile(`public/images/products/${file.filename}`);
      // unlinkSync 파일 삭제
      fs.unlinkSync(`public/images/products/${file.filename}`);
    })
  );
  next();
};

const blogImgResize = async (req, res, next) => {
  if (!req.files) return next();
  await Promise.all(
    req.files.map(async (file) => {
      await sharp(file.path)
        .resize(300, 300)
        .toFormat("jpeg")
        .jpeg({ quality: 90 })
        .toFile(`public/images/blogs/${file.filename}`);
      // unlinkSync 파일 삭제
      fs.unlinkSync(`public/images/blogs/${file.filename}`);
    })
  );
  next();
};

module.exports = {
  uploadPhoto,
  productImgResize,
  blogImgResize
};