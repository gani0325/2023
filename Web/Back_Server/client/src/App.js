import { useEffect, useState } from "react";
import axios from "axios";

// 기본 제공하는 api는 fetch
// axios 라이브러리

const SERVER_URL = "http://localhost:8080/api/todo";
// 프론트가 서버에 데이터 요청하려면 "서버주소", "http 메소드" 필요
function App() {
  const [todoList, setTodoList] = useState([]);
  // axios 이용하여 데이터 응답 받기
  const fetchData = async () => {
    // 응답 보내기 -> 응답 오면 setTolist에 넣기
    const response = await axios.get(SERVER_URL);
    setTodoList(response.data);
  };

  useEffect(() => {
    fetchData();
  }, []);

  // 데이터 추가하고 서버에 POST 요청
  const onSubmitHandler = async (e) => {
    e.preventDefault();
    const text = e.target.text.value;
    const done = e.target.done.checked;

    // axios 이용하여 데이터 보내기
    await axios.post(SERVER_URL, { text, done });
    fetchData();
  };

  return (
    <div className="App">
      <h1>TODO LIST</h1>
      <form onSubmit={onSubmitHandler}>
        <input name="text" />
        <input name="done" type="checkbox" />
        <input type="submit" value="추가" />
      </form>
      {/* 조회하는 곳 */}
      {todoList.map((todo) => (
        <div key={todo.id} style={{ display: "flex" }}>
          <div>{todo.id}</div>
          <div>{todo.text}</div>
          <div>{todo.done ? "Y" : "N"}</div>
        </div>
      ))}
    </div>
  );
}

export default App;
