const express = require("express");
const expressLayouts = require("express-ejs-layouts");

const app = express();

// ejs 미들웨어
app.use(expressLayouts);
// express 의 view 엔진을 ejs 로 세팅
app.set("view engine", "ejs");
// img
app.use(express.static('public'));

// Routes
app.use("/", require("./routes/index"));
app.use("/users", require("./routes/user"));

const PORT = process.env.PORT || 8000;

app.listen(PORT, console.log(`🚀Server started on port http://localhost:${PORT}`));