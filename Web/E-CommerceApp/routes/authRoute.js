const express = require("express");
const router = express.Router();
const {createUser, loginCheck} = require("../controllers/userCtrl");

router.post("/register", createUser);
router.post("/login", loginCheck);

module.exports = router;