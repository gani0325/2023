// express : http 모듈 내장되어서 서버의 역할
const express = require("express");
const app = express();
require("dotenv").config();

// 서버가 실행될 포트
// app.set("키, 값") : 데이터 저장
app.set("port", process.env.PORT || 3000);

// app.get("주소, 라우터") : 주소에 대한 GET 요청이 올 때 어떤 동작 할지 적기
app.get("/", (req, res) => {
    res.send("Hello express");
});

// HTTP 웹 서버와 동일
app.listen(app.get("port"), () => {
    console.log(app.get("port"), "빈 포트에서 대기중");
});