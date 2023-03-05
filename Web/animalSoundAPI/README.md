# Node.js, npm 모듈 등 기초에 대해 배우고, express 프레임워크로 자바스크립트 API를 구현하는 것을 실습
- (유튜브 조코딩 참고)

## ⭐ 패키지
### npm init
- npm 을 시작하겠다
### npm install figlet --save
- 모듈 설치
- 뒤에 -g 넣으면 내 컴퓨터 전체에서 가능
### package-lock.json
- 내용 상세하게
### package.json
- 내용 대략적

---
## ⭐ 기본 함수 및 메소드
### express
- node.js 기반의 웹 프레임워크 (요청에 따라 응답)
### HTTP 메소드
- 요청의 목적, 종류를 알려주기 위해 사용하는 수단
### GET
- 주소창에서 데이터 전달
### POST
- 내부적으로 body에 데이터 전달
### 콜백함수
- 함수(끝나고 실행할 함수)
- 다른 코드의 인수로서 넘겨주는 실행 가능한 코드
### axios : express 요청 보냄
### json : javascript object notaion

---
## ⭐ HTTP 메소드
### GET(주소창) : params, query 
- params : 변수로 받음 (user/:id), 
- q = req.params
- query : (key : value)
### POST(axios, fetch) : params, body
- params : 변수 받음 (user/:id)
- body 

---
## ⭐CORS
- 서버의 응답이 왔을 때 브라우저가 요청한 Origin 과 응답한 헤더 Access-Control-Request-Headers 의 값을 비교하여 유효한 요청이라면 리소스를 응답
- HTML의 요청을 응답 잘되도록