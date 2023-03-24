const express = require("express");
require("dotenv").config();
const PORT = process.env.PORT || 8000;
const path = require("path");
const app = express();

// get(주소, 라우터) : 주소에 대한 요청이 올 때 어떤 동작을 하나
app.get("/", (req, res) => {
    // 1) app.js 로 서버 열기
    // res.send("Express study");
    
    // 2) index.html 로 서버 열기
    res.sendFile(path.join(__dirname, "/index.html"));
});

// listen = http 웹 서버
app.listen(PORT, () => {
    console.log(`🚀 Server started on port http://localhost:${PORT}`);
});