const express = require("express");
const router = express.Router();

// Main page
router.get("/", (req, res) => {
    res.send("Welcome home");
});

module.exports = router;