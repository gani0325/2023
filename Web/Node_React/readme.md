# react와 node 연동하기

## 1) react

: HTML을 이쁘게 만들어주는 툴

- npx create-react-app react-project
- App.js 만들고 개발하기 npm run start
- 개발 끝난다면 -> npm run build
- -> html 파일 (main page) 이 생성

## 2) node

- server.js 만들기
- npm init -y
- npm install express nodemon cors
- server 실행하기 -> nodemon server.js

## 3) db 데이터를 서버를 통해 react로 보내기

- 받은 데이터로 react가 html 생성하기
- html 을 서버가 만들면 server-side rendering
- htlm 을 리액트가 만들면 client-side rendering
  - react-router-dom
