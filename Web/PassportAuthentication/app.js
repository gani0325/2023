const express = require("express");
const expressLayouts = require("express-ejs-layouts");
const mongoose = require("mongoose");
require("dotenv").config();

const app = express();

// DB config
const db = process.env.MONGODB_URI;

// connect to Mongo
mongoose.connect(process.env.MONGODB_URI,{ 
  useNewUrlParser: true,    // useNewUrlParser : 에러 방지
  useUnifiedTopology: true
})
  .then(()=> console.log("💚MongoDB Connected..."))
  .catch(err => console.log(err));


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