const express = require("express");
const articleRouter = require("./routes/articles");
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

// router
app.use("/article", articleRouter);

app.get("/", (req, res) => {
  const articles = [
    {
      title: "Test article1",
      createdAt: new Date(),
      description: "Test description1",
    },
    {
      title: "Test article2",
      createdAt: new Date(),
      description: "Test description2",
    },
  ];
  res.render("articles/index", { articles: articles });
});

app.listen(3000);
