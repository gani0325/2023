const express = require("express");
const { createProduct, getProduct } = require("../controllers/productCtrl");
const router = express.Router();

router.post("/", createProduct);
router.get("/", getProduct);

module.exports = router;