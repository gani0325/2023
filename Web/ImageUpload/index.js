// imports
require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const session = require("express-session");
// express-session 
// 1. 파일에 저장
// 2. DB에 저장
// 3. Memory 에 저장

const app = express();
const PORT = process.env.PORT || 8000;

// Database 연결
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });   // useNewUrlParser : 에러 방지
const db = mongoose.connection;
db.on("error", (error) => console.log(error));
db.once("open", () => console.log("💚 Connected to the database!"));

// Middleware 연결
app.use(express.urlencoded({ extended: false }));
app.use(express.json());        // JSON형태의 데이터를 해석
app.use(session({
  secret: process.env.SECRET,   // 암호화를 위한 keygen. 보통 env에 넣어서 전달
  saveUninitialized: true,      // 세션에 저장할 내역이 없더라도 처음부터 세션을 생성할지 설정
  resave: false,                // 세션을 언제나 저장할지 설정함 
  cookie: {                     // 쿠키의 유효시간
    maxAge: 86400000,           // 24 hours (= 24 * 60 * 60 * 1000 ms)
  },
})
);

// 공통 EJS 파일(header나 footer)에서 사용할 데이터를 세팅
app.use((req, res, next) => {
  // ejs 파일에서 사용하려면 'res.locals.변수명 = 값' 을 이용
  res.locals.message = req.session.message;
  delete req.session.message;
  next();         // 앱 내의 그 다음 미들웨어 함수가 호출
});

// uploads 폴더의 사진 html에 보이게 하기
app.use(express.static("uploads"));

// set template engine
app.set("view engine", "ejs");

// router
app.use("", require("./routes/routes"));

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(PORT, () => {
  console.log(`server started at 🚀 http://localhost:${PORT}`);
});