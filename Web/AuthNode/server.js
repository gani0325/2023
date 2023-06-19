const express = require("express");
const session = require("express-session");
const app = express();

// 모든 uri에 접근 했을 때 적용되도록 라우터를 만듦
app.use(
  session({
    // 암호화에 대한 내용
    secret: "key that all sign cookie",
    // 매 request 마다 세션을 계속 다시 저장
    resave: false,
    // request에서 새로 생성된 session에 아무런 작업이 이루어지지 않은 상황
    saveUninitialized: false,
  })
);

app.get("/", (req, res) => {
  req.session.isAuth = true;
  console.log(req.session);
  console.log(req.session.id);
  res.send("Hello sessions");
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
