const express = require("express");
const app = express();
const path = require("path");

app.listen(8080, function () {
  console.log("listening on 8080");
});

// 리액트와 nodejs 서버간 ajax 요청
app.use(express.json()); // 유저가 보낸 array/object 데이터를 출력해보기 위해 필요
var cors = require("cors"); // 다른 도메인주소끼리 ajax 요청 주고받을 때 필요
app.use(cors);

// static 을 이용하여 특정 폴더의 파일들 전송 가능
app.use(express.static(path.join(__dirname, "react-project/build")));

app.get("/", function (req, res) {
  // res.sendFile(path.join(__dirname, "리액트로 만든 html 파일 경로"));
  res.sendFile(path.join(__dirname, "react-project/build/index.html"));
});

// db 데이터 뽑아서 보내주는 API
// ex) db 에 있는 상품명 보여준다면
app.get("/product", function (req, res) {
  res.json({ name: "상품명" });
});

// react router 쓰는 경우 최하단에 추가 하기
app.get("*", function (req, res) {
  // res.sendFile(path.join(__dirname, "리액트로 만든 html 파일 경로"));
  res.sendFile(path.join(__dirname, "react-project/build/index.html"));
});
