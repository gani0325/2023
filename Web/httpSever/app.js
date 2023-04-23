// express : http 모듈 내장되어서 서버의 역할
const express = require("express");
const app = express();
// 파일 경로
const path = require("path");
require("dotenv").config();

// 서버가 실행될 포트
// app.set("키, 값") : 데이터 저장
app.set("port", process.env.PORT || 3000);

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