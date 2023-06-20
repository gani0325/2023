# Understanding Authentication in Node.js - Sessions &Cookies

1. 쿠키 (cookie) <br>
   - 웹 서버가 브라우저에게 지시하여 사용자의 로컬 컴퓨터에 파일 또는 메모리에 저장하는 작은 기록 정보 파일
2. 세션 HTTP Session <br>
   - HTTP Session id를 식별자로 구별하여 데이터를 사용자의 브라우저에 쿠키형태가 아닌 접속한 서버 DB에 정보를 저장
   - 클라이언트는 HTTP Session id를 쿠키로 메모리 저장된 형태로 가지고 있음
   - 메모리에 저장하기 때문에 브라우저가 종료되면 사라짐
3. login / register / dashboard / home page 설정 <br>
   ➡️ home
   ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbv5KP6%2FbtskDj7qQAV%2FV7rPh6LH6Gpfkgo4Hr021K%2Fimg.png)
   ➡️ register
   ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Flykg6%2FbtskJqLcIC7%2FD7kKYQEeCfqInk2HVTGUyk%2Fimg.png)
   ➡️ login
   ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FEz82I%2FbtskC3cAdVy%2FFG8jJV14phmI0m04iKGIK1%2Fimg.png)
   ➡️ dashboard
   ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FOq4OA%2FbtskEU7oTqb%2FPAS4gJRq2Qm8xkvBIvToFk%2Fimg.png)
   ➡️ mongoDB
   ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FqVucX%2FbtskJiT0zsg%2FnSlkuJ400VPam4CXstngSk%2Fimg.png)
