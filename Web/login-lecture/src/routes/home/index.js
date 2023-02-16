"use strict";

const express = require("express");
const router = express.Router();

// 받아오기 (컨트롤러)
const ctrl = require("./home.ctrl");

// 컨트롤러 안에 있는 객체 불러오기!
router.get("/", ctrl.hello);
router.get("/login", ctrl.login);

router.post("/login", ctrl.login);

// 내보내기
module.exports = router;