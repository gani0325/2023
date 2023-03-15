const express = require("express");
const expressLayouts = require("express-ejs-layouts");
const mongoose = require("mongoose");
require("dotenv").config();

const app = express();

// DB config
const db = process.env.MONGODB_URI;

// connect to Mongo
mongoose.connect(db,{ 
  useNewUrlParser: true,    // useNewUrlParser : 에러 방지
  useUnifiedTopology: true
})
  .then(()=> console.log("💚MongoDB Connected..."))
  .catch(err => console.log(err));

// ejs 미들웨어
app.use(expressLayouts);
// express 의 view 엔진을 ejs 로 세팅
app.set("view engine", "ejs");

// Bodyparser : express서버로 POST요청을 할 때 input태그의 value를 전달
// URL-encoded 형식의 문자열로 넘어오기 때문에 객체로의 변환 필요
app.use(express.urlencoded({ extended : false }));

// muploads 폴더의 사진 html에 보이게 하기g
app.use(express.static('public'));

// Routes
app.use("/", require("./routes/index"));
app.use("/users", require("./routes/user"));

const PORT = process.env.PORT || 8000;

app.listen(PORT, console.log(`🚀Server started on port http://localhost:${PORT}`));