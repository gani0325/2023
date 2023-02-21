"use strict";
// const UserSchema = require("../../models/UserSchema");
const User = require("../../models/User");
const logger = require("../../config/logger");

// GET
const output = {
    home : (req, res) => {        
        logger.info(`GET / 200 "홈 화면 이동"`);
        res.render("home/index");
    },
    login : (req, res) => {
        logger.info(`GET / login 200 "로그인 화면 이동"`);
        res.render("home/login");
    },
    register : (req, res) => {
        logger.info(`GET / register 200 "회원가입 화면 이동"`);
        res.render("home/register");
    }
}

// POST
const process = {
    login : async (req, res) => {
        // user 인스턴스가 login 하면 response 받음
        // json 형태로 response 응답한다
        const user = new User(req.body);
        const response = await user.login();    // async await 함수는 자체적으로 promise

        if (!response.err)
            logger.info(`POST / login 200 Response : "success : ${response.success}, ${response.err}`);
        else
            logger.info(`POST / login 200 Response : "success : ${response.success}, msg : ${response.msg}`);
        
        return res.json(response);
    },

    register : async (req, res) => {
        // user 인스턴스가 login 하면 response 받음
        // json 형태로 response 응답한다
        const user = new User(req.body);
        const response = await user.register();
        
        if (!response.err)
            logger.info(`POST / register 200 Response : "success : ${response.success}, ${response.err}`);
        else
            logger.info(`POST / register 200 Response : "success : ${response.success}, msg : ${response.msg}`);


        return res.json(response);
    },
}

// 꼭 밖으로 호출하기
module.exports = {
    output,
    process,
};