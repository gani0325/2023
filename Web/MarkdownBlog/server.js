const express = require("express");
const articleRouter = require("./routes/articles");
const Article = require("./models/article");
const mongoose = require("mongoose");
const app = express();

require("dotenv").config();

// DB config
const db = process.env.MONGODB_URI;

// connect to Mongo
mongoose
  .connect(db, {
    useNewUrlParser: true, // useNewUrlParser : 에러 방지
    useUnifiedTopology: true,
  })
  .then(() => console.log("💚MongoDB Connected..."))
  .catch((err) => console.log(err));

app.set("view engine", "ejs");

app.use(express.urlencoded({ extended: false }));

app.get("/", async (req, res) => {
  const articles = await Article.find().sort({
    createdAt: "desc",
  });
  res.render("articles/index", { articles: articles });
});

// router
app.use("/articles", articleRouter);

app.listen(3000);
