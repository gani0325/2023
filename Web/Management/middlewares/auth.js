'use strict';

const dotenv = require('dotenv');
// JWT(JSON Web Token - JSON 웹 토큰)은 두 개체 사이에서 안전하게 클레임을 전달(표현)
// 1) HEADER(헤더) typ : 토큰의 타입을 지정(JWT), alg : 해싱 알고리즘을 지정
// 2) PAYLOAD(내용) - 사용되는 정보의 한 조각을 클레임(claim)
// 3) VERIFY SIGNATURE(서명) : header + payload 정보를 비밀키로 해쉬를 하여 생성!
const jwt = require("jsonwebtoken");
dotenv.config();
// 로그인 시 해당 id, pw와 일치하는 요청이 들어오면 access token과 refresh token을 발급
// 발급된 token은 클라이언트에서 요청을 보낼 때마다 
// headers에 authorization: 'bearer ' + accessToken 방식으로 넘겨받아 해당 요청의 token이 유효한지 검사

function authenticateToken(req, res, next) {
    // access token의 유효성 검사
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[0];

    if (token == null) {
        console.log("잘못된 token이다!!!")
        return res.sendStatus(401);
    }
    // verify를 통해 값 decode
    jwt.verify(token, "Snippet_SecretKEY", (err, user) => {
        if(err) return res.sendStatus(403);
        req.user = user;
        next();
    });
};

function generateAccessToken(username) {
    // sign 메소드를 통해 access token 발급 (process.env.ACCESS_TOKEN_SECRET)
    return jwt.sign({data : username},"Snippet_SecretKEY", {
        expiresIn : "1h"
    });
};

module.exports = {
    authenticateToken,
    generateAccessToken,
};