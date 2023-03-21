const express = require("express");
const router = express.Router();
const {createUser, loginCheck, getAllUsers, getAUsers} = require("../controllers/userCtrl");

router.post("/register", createUser);
router.post("/login", loginCheck);
router.get("/all-users", getAllUsers);
router.get("/:id", getAUsers);

module.exports = router;