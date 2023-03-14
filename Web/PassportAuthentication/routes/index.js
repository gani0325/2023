const express = require("express");
const router = express.Router();

// Main page
router.get("/", (req, res) => {
    // rednering 할 때 view의 파일 이름 써야됨
    res.render("welcome");
});

module.exports = router;