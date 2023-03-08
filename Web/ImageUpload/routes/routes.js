const express = require("express");
const router = express.Router();

// Home (ejs 와 연동)
router.get("/", (req, res) => {
  res.render("index", { title : "Home" });
});

router.get("/add", (req, res) => {
  res.render("addUsers", { title : "Add users" });
})

module.exports = router;