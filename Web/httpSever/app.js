// express : http 모듈 내장되어서 서버의 역할
const express = require("express");
const app = express();
// process.env 관리
const dotenv = require("dotenv");
// 미들웨어
const cookieParser = require("cookie-parser");
const session = require("express-session");
const morgan = require("morgan");
// 파일 경로
const path = require("path");
require("dotenv").config();

dotenv.config();
// 서버가 실행될 포트
// app.set("키, 값") : 데이터 저장
app.set("port", process.env.PORT || 8000);

// dev : [HTTP 메서드][주소][HTTP 상태 코드][응답 코드]-[응답 바이트]
app.use(morgan("dev"));
app.use("/", express.static(path.join(__dirname, "public")));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret: process.env.COOKIE_SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  },
  name: "session-cookie",
}));

// 미들웨어 : 요청과 응답을 조정
// 요청, 응답, 다음 미들에ㅜ어로 넘어가기
app.use((req, res, next) => {
  console.log("모든 요청에 다 실행됨");
  next();
});

app.get("/", (req, res, next) => {
  console.log("GET / 요청에서만 실행");
  next();
}, (req, res) => {
  throw new Error("에러는 에러 처리 미들웨어로 간다");
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).send(err.message);
});

// HTTP 웹 서버와 동일
app.listen(app.get("port"), () => {
  console.log(app.get("port"), "빈 포트에서 대기중");
});