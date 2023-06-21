const express = require("express");
const articleRouter = require("./routes/articles");
const app = express();

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
  res.render("index", { articles: articles });
});

app.listen(3000);
