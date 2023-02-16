"use strict";
// const UserSchema = require("../../models/UserSchema");
const User = require("../../models/User");

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
        // user 인스턴스가 login 하면 response 받음
        // json 형태로 response 응답한다
        const user = new User(req.body);
        const response = user.login();
        console.log(response);

        return res.json(response);
    },
}

// 꼭 밖으로 호출하기
module.exports = {
    output,
    process,
};