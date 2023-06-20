const express = require("express");
const session = require("express-session");
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

//=================== Routes
// Landing Page
app.get("/", (req, res) => {
  res.render("landing");
});

// // Login Page
app.get("/login", (req, res) => {
  res.render("login");
});
app.post("/login", (req, res) => {});

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

  user = new UserModel({
    username,
    email,
    password,
  });
});

// // Dashboard Page
app.get("/dashboard", (req, res) => {
  res.render("dashboard");
});

app.post("/logout", (req, res) => {});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
