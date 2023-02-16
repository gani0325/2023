"use strict";

// 모듈
const express = require("express");
const app = express();

// 라우터
const home = require("./src/routes/home");

// 앱 세팅
app.set("views", "./src/views");
app.set("view engine", "ejs");

// ejs 에서 js 파일 받아올 수 있도록 미들웨어
app.use(express.static(`${__dirname}/src/public`))
// routes 꺼 받아오기
app.use("/", home);      // use -> 미들 웨어를 등록해주는 메서드


// app.js 내보내기
module.exports = app;