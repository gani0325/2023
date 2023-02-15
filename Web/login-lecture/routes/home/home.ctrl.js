"use strict";

const hello = (req, res) => {
    res.render("home/index");
};

const login = (req, res) => {
    res.render("home/login");
};

// 꼭 밖으로 호출하기
module.exports = {
    hello,
    login,
};