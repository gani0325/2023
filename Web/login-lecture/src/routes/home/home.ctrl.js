"use strict";

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
        console.log(req.body);
    },
}

// 꼭 밖으로 호출하기
module.exports = {
    output,
    process,
};