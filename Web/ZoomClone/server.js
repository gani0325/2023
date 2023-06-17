const express = require("express");
const app = express();
const server = require("http").Server(app);
// UUID : 범용 고유 식별자를 의미하며 중복이 되지 않는 유일한 값을 구성
const { v4: uuidv4 } = require("uuid");

// EJS
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.redirect(`/${uuidv4()}`);
});

app.get("/:room", (req, res) => {
  res.render("room", { roomId: req.params.room });
});

server.listen(3030);
