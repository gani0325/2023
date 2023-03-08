const express = require("express");
const router = express.Router();

// local~~/users 에서 응답
router.get("/users", (req, res) => {
    res.send("All users");
});

module.exports = router;