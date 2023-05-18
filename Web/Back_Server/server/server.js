const express = require("express");
const app = express();

// body-parser
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// 데이터를 서버에 저장해놓음 (데이터베이스 생략)
let id = 2;
const todoList = [
  {
    id: 1,
    text: "할일 1",
    done: false,
  },
];

app.get("/", function (res, res) {
  res.send("server");
});

// todolist 조회
app.get("/api/todo", (req, res) => {
  res.json(todoList);
});

// todolist 등록
app.post("/api/todo", (req, res) => {
  // body 에 데이터 넣어 전송
  const { text, done } = req.body;
  todoList.push({
    id: id++,
    text,
    done,
  });
  return res.send("success");
});

app.listen(8080, () => {
  console.log("listen on 8080");
});
