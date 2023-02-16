"use strict";
const UserSchema = require("../../models/UserSchema");

const output = {
    home : (req, res) => {
        res.render("home/index");
    },
    
    login : (req, res) => {
        res.render("home/login");
    },
}

const process = {
    login : (req, res) => {
        const id = req.body.id;
        const pw = req.body.pw;

        // 모든 login 값 가져오기 (로그인 검증)
        const users = UserSchema.getUsers("id", "pw");
        const response = {};

        // id가 users.id에 있을경우
        if (users.id.includes(id)) {
            const idx = users.id.indexOf(id);
            if (users.pw[idx] === pw) {
                response.success = true;
                return res.json(response);
            }
        }
        response.success = false;
        response.msg = "로그인에 실패하셨습니다."
        return res.json(response);
    },
}

// 꼭 밖으로 호출하기
module.exports = {
    output,
    process,
};