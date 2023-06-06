const express = require("express");
const app = express();

app.use("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.listen(8080);

// 웹소켓 연결
const WebSocket = require("ws");
const socket = new WebSocket.Server({
  port: 8081,
});

// 웹소켓으로 오는 유저 메시지 받기
socket.on("connection", (ws, req) => {
  ws.on("message", (msg) => {
    console.log("User Message : " + msg);
    // 웹소켓으로 서버 -> 유저 메시지 보내기
    ws.send("fighting!!");
  });
});
