const express = require("express");
require("dotenv").config();
const PORT = process.env.PORT || 8000;
const path = require("path");
const app = express();

app.use((req, res, next) => {
  console.log("모든 요청에 다 실행됨");
  // next : 다음 미들웨어로 간다
  next();
});

// get(주소, 라우터) : 주소에 대한 요청이 올 때 어떤 동작을 하나
app.get("/", (req, res, next) => {

  console.log("GET / 요청에서만 실행");
  next();
}, (req, res) => {
  throw new Error("Error는 Error 처리 Middleware로 간다");
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).send(err.message);
});

// listen = http 웹 서버
app.listen(PORT, () => {
  console.log(`🚀 Server started on port http://localhost:${PORT}`);
});