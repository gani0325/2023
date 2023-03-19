const express = require("express");
const expressLayouts = require("express-ejs-layouts");
const mongoose = require("mongoose");
const flash = require("connect-flash");
const session = require("express-session");
const passport = require("passport");
const app = express();

require("dotenv").config();
require("./middlewares/passport")(passport);

// DB config
const db = process.env.MONGODB_URI;

// connect to Mongo
mongoose.connect(db, {
  useNewUrlParser: true,    // useNewUrlParser : 에러 방지
  useUnifiedTopology: true
})
  .then(() => console.log("💚MongoDB Connected..."))
  .catch(err => console.log(err));

// ejs 미들웨어
app.use(expressLayouts);
// express 의 view 엔진을 ejs 로 세팅
app.set("view engine", "ejs");

// Bodyparser
// express서버로 POST요청을 할 때 input태그의 value를 전달
// URL-encoded 형식의 문자열로 넘어오기 때문에 객체로의 변환 필요
app.use(express.urlencoded({ extended: false }));

// Express session
// Express 프레임워크에서 세션을 관리하기 위한 미들웨어
// Server에서 Client에게 쿠키로 sessionID를 발급해주고,
// 이 쿠키를 통해 Server에 접속하면 sessionID값을 활용해 어떤 Client인지 식별하고 관련 정보를 제공
app.use(session({
  secret: 'secret',
  resave: true,
  saveUninitialized: true,
}));

// passport 초기화 및 session 연결 미들웨어
app.use(passport.authenticate('session'));
app.use(passport.initialize());
app.use(passport.session());

// Connect flash
// 한 번 출력되고 사라지는 메시지
// session 보다 아래쪽에서 미들웨어를 설치
// flash 메시지는 Queue처럼 데이터를 꺼내는 즉시, session에서 삭제
app.use(flash());

// Global Vars
app.use((req, res, next) => {
  // res.locals : 뷰를 렌더링하는 기본 콘텍스트를 포함하는 객체
  res.locals.success_msg = req.flash("success_msg");
  res.locals.error_msg = req.flash("error_msg");
  res.locals.error = req.flash("error");
  next();
});

// uploads 폴더의 사진 html에 보이게 하기g
app.use(express.static('public'));

// Routes
app.use("/", require("./routes/index"));
app.use("/users", require("./routes/user"));

const PORT = process.env.PORT || 8000;

app.listen(PORT, console.log(`🚀Server started on port http://localhost:${PORT}`));