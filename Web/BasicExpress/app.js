const express = require("express");
require("dotenv").config();
const path = require("path");
const morgan = require("morgan");
const cookiePraser = require("cookie-parser");
const session = require("express-session");
const indexRouter = require("./routes/index");
const userRouter = require("./routes/user");

const PORT = process.env.PORT || 8000;
const app = express();

app.use(morgan("dev"));
app.use("/", express.static(path.join(__dirname, "public")));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookiePraser(process.env.SECRET));
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret: process.env.SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  },
  name: "session-cookie",
}));


app.use((req, res, next) => {
  console.log("모든 요청에 다 실행됨");
  // next : 다음 미들웨어로 간다
  next();
});

app.use("/", indexRouter);
app.use("/user", userRouter);

// listen = http 웹 서버
app.listen(PORT, () => {
  console.log(`🚀 Server started on port http://localhost:${PORT}`);
});