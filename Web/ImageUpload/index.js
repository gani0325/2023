// imports
require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const session = require("express-session");

const app = express();
const PORT = process.env.PORT || 8000;

// Database 연결
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });   // useNewUrlParser : 에러 방지
const db = mongoose.connection;
db.on("error", (error) => console.log(error));
db.once("open", () => console.log("💚 Connected to the database!"));

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(PORT, () => {
  console.log(`server started at 🚀 http://localhost:${PORT}`);
});