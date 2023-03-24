const express = require("express");
require("dotenv").config();
const path = require("path");
const morgan = require("morgan");
const cookiePraser = require("cookie-parser");
const session = require("express-session");
const multer = require("multer");

const PORT = process.env.PORT || 8000;
const app = express();

app.use(morgan("dev"));
app.use("/", express.static(path.join(__dirname, "public")));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookiePraser(process.env.SECRET));
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret: process.env.SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  },
  name: "session-cookie",
}));

const upload = multer({
  storage: multer.diskStorage({
    // 어디에 어떤 이름으로 저장되는지
    destination(req, file, done) {
      done(null, "uploads/");
    },
    filename(req, file, done) {
      const ext = path.extname(file.originalname);
      done(null, path.basename(file.originalname, ext) + Date.now() + ext);
    },
  }),
  limits: { fileSize: 5 * 1024 * 1024 },
});

app.get("/upload", (req, res) => {
  res.sendFile(path.join(__dirname, "multipart.html"));
});

app.post("/upload",
  upload.fields([{ name: "image1" }, { name: "image2" }]),
  (req, res) => {
    console.log(req.files, req.body);
    res.send("ok");
  },
);

app.use((req, res, next) => {
  console.log("모든 요청에 다 실행됨");
  // next : 다음 미들웨어로 간다
  next();
});

// listen = http 웹 서버
app.listen(PORT, () => {
  console.log(`🚀 Server started on port http://localhost:${PORT}`);
});