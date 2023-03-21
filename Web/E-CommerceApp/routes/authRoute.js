const express = require("express");
const router = express.Router();
const {createUser, loginCheck, getAllUsers} = require("../controllers/userCtrl");

router.post("/register", createUser);
router.post("/login", loginCheck);
router.get("/all-users", getAllUsers);

module.exports = router;