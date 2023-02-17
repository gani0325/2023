"use strict";

const express = require("express");
const router = express.Router();

// 받아오기 (컨트롤러)
const ctrl = require("./home.ctrl");

// 컨트롤러 안에 있는 객체 불러오기!
router.get("/", ctrl.output.home);
router.get("/login", ctrl.output.login);        // 로그인 화면
router.get("/register", ctrl.output.register);     // 회원가입 화면

router.post("/login", ctrl.process.login);
router.post("/register", ctrl.process.register);     // 회원가입

// 내보내기
module.exports = router;