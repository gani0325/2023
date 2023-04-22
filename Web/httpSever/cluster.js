// 싱글 프로세스로 동작하는 노드가 CPU 코어를 모두 사용
const cluster = require("cluster");
const http = require("http");
const numCPUs = require("os").cpus().length;

if (cluster.isMaster) {
  console.log(`마스터 프로세스 아이디 : $ {process.pid}`);
  // CPU 개수만큼 워커 생산
  for (let i = 0; i < numCPUs; i += 1) {
    cluster.fork();
  }
  // 워커 종료되었을 때
  cluster.on("exit", (worker, code, signal) => {
    console.log(`${worker.process.pid}번 워커가 종료되었습니다.`);
    console.log("code", code, "signal", signal);
  });
} else {
  // 워커들이 포트에서 대기
  http.createServer((req, res) => {
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
    setTimeout(() => {
      // 워커가 존재하는지 확인하기 위해 1초마다 강제 종료
      process.exit(1);
    }, 1000);

  }).listen(8086);

  console.log(`${process.pid}번 워커 실행`);
}