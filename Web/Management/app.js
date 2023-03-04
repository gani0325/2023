'use strict';

const express = require("express");
const mongoose = require("mongoose");
const dbConfig = require("./config/db.config");

const dotenv = require('dotenv');
dotenv.config();

const auth = require("./middlewares/auth");
const errors = require("./middlewares/errors");

const {unless} = require("express-unless");

const app = express();

// 데이터베이스에 요청
mongoose.Promise = global.Promise;
mongoose.connect(dbConfig.db, {
    // useNewUrlParser, useUnifiedTopology 옵션은 서버 실행 시 발생되는 오류를 제거
    useNewUrlParser : true,
    useUnifiedTopology : true
}).then(
    () => {
        console.log("db 연결 성공")
    },
    (error) => {
        console.log("db 연결 안됨 : " + error);
    } 
);

// authenticateToken : 미들웨어 - 보호된 경로에 액세스하기 전에 토큰을 인증

auth.authenticateToken.unless = unless
console.log(auth.authenticateToken.unless);
app.use(auth.authenticateToken.unless({
    path: [
        { url: '/users/login', methods: ['POST']},
        { url: '/users/register', methods: ['POST']}
    ]
}));

// 클라이언트로 부터 받은 http 요청 메시지 형식에서 body데이터를 해석
app.use(express.json());

app.use("/users", require("./routes/user.routes"));

app.use(errors.errorHandler);

app.listen(process.env.PORT || 4000, function() {
    console.log("🚀 시작해볼까!")
})