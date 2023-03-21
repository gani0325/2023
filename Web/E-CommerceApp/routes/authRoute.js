const express = require("express");
const router = express.Router();
const {createUser, loginCheck, getAllUsers, getAUsers, deleteAUser} = require("../controllers/userCtrl");

router.post("/register", createUser);
router.post("/login", loginCheck);
router.get("/all-users", getAllUsers);
router.get("/:id", getAUsers);
router.delete("/:id", deleteAUser);

module.exports = router;