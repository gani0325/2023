const express = require("express");
const expressLayouts = require("express-ejs-layouts");

const app = express();

// ejs 미들웨어
app.use(expressLayouts);
// express 의 view 엔진을 ejs 로 세팅
app.set("view engine", "ejs");
//  set 을 한 부분은 layout 폴더의 layout 파일을 사용하겠다는 선언
// Routes
app.use("/", require("./routes/index"));
app.use("/users", require("./routes/user"));

const PORT = process.env.PORT || 8000;

app.listen(PORT, console.log(`🚀Server started on port http://localhost:${PORT}`));