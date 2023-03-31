const express = require("express");
const bodyParser = require("body-parser");
const dbConnect = require("./config/dbConnect");
const {notFound, errorHandler} = require("./middlewares/errorHandler");
const app = express();
require("dotenv").config();
const PORT = process.env.PORT || 8000;

const authRouter = require("./routes/authRoute");
const productRouter = require("./routes/productRoute");
const blogRouter = require("./routes/blogRoute");
const prodCategoryRouter = require("./routes/prodCategoryRoute");
const blogCategoryRouter = require("./routes/blogCategoryRoute");
const brandRouter = require("./routes/brandRoute");
const cookieParser = require("cookie-parser");

// mongoDB
dbConnect();
// Bodyparser
// express서버로 POST요청을 할 때 input태그의 value를 전달
// URL-encoded 형식의 문자열로 넘어오기 때문에 객체로의 변환 필요
app.use(bodyParser.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.use("/api/user", authRouter);
app.use("/api/product", productRouter);
app.use("/api/blog", blogRouter);
app.use("/api/prodCategory", prodCategoryRouter);
app.use("/api/blogCategory", blogCategoryRouter);
app.use("/api/brand", brandRouter);

app.use(notFound);
app.use(errorHandler);

app.use("/", (req, res) => {
  res.send("hihi");
})

app.listen(PORT, () => {
    console.log(`🚀 Server started on port http://localhost:${PORT}`);
});