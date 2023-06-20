const express = require("express");
const session = require("express-session");
const bcrypt = require("bcryptjs");
const mongoose = require("mongoose");
const MongoDBSession = require("connect-mongodb-session")(session);
const app = express();

// DB config
require("dotenv").config();
const db = process.env.MONGODB_URI;

const UserModel = require("./models/User");

// connect to Mongo
mongoose
  .connect(db, {
    useNewUrlParser: true, // useNewUrlParser : 에러 방지
    useUnifiedTopology: true,
  })
  .then((req) => console.log("💚MongoDB Connected..."))
  .catch((err) => console.log(err));

const store = new MongoDBSession({
  url: db,
  collection: "mySessions",
});

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

// 모든 uri에 접근 했을 때 적용되도록 라우터를 만듦
app.use(
  session({
    // 암호화에 대한 내용
    secret: "key that all sign cookie",
    // 매 request 마다 세션을 계속 다시 저장
    resave: false,
    // request에서 새로 생성된 session에 아무런 작업이 이루어지지 않은 상황
    saveUninitialized: false,
    store: store,
  })
);

const isAuth = (req, res, next) => {
  if (req.session.isAuth) {
    next();
  } else {
    res.redirect("/login");
  }
};

//=================== Routes
// Landing Page
app.get("/", (req, res) => {
  res.render("landing");
});

// // Login Page
app.get("/login", (req, res) => {
  res.render("login");
});
app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  const user = await UserModel.findOne({ email });

  // 가입되지 않은 사용자라면
  if (!user) {
    return res.redirect("/login");
  }

  // 비밀번호가 틀렸다면
  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) {
    return res.redirect("/login");
  }

  req.session.isAuth = true;
  res.redirect("/dashboard");
});

// // Register Page
app.get("/register", (req, res) => {
  res.render("register");
});
app.post("/register", async (req, res) => {
  const { username, email, password } = req.body;

  let user = await UserModel.findOne({ email });

  if (user) {
    return res.redirect("/register");
  }

  const hashedPsw = await bcrypt.hash(password, 12);

  user = new UserModel({
    username,
    email,
    password: hashedPsw,
  });

  await user.save();

  res.redirect("/login");
});

// // Dashboard Page
app.get("/dashboard", isAuth, (req, res) => {
  res.render("dashboard");
});

// // Logout Page
app.post("/logout", (req, res) => {
  req.session.destroy((err) => {
    if (err) throw err;
    res.redirect("/");
  });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
