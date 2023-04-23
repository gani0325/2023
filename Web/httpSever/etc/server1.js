// http : 웹 브라우저의 요청 처리
const http = require("http");

// 요청에 대한 콜백 함수
http.createServer((req, res) => {
  // writeHead : 응답에 대한 정보를 기록하는 메서드
  // 1) 200 : 성공 요청 메소드
  // 2) 응답에 대한 정보를 보내는데 콘텐츠 형색이 HTML
  // 3) 한글 표시를 위해 utf-8 지정
  // 위 세가지의 정보 기록되는 부분을 헤더
  res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  // 클라이언트로 보낼 데이터 
  // 데이터 기록되는 부분을 본문 
  res.write("<h1>Hello node!</h1>");
  // 응답을 종하는 메서드
  res.end("<p>Hello Server!</p>");
})

server.listen(8080);

server.on("listening", () => {
  console.log("8080번 포트에서 서버 대기중");
});

server.on("error", (error) => {
  console.log(error);
})