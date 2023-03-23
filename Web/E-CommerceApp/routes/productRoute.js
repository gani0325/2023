const express = require("express");
const { createProduct, getAProduct, getAllProduct, updateProduct } = require("../controllers/productCtrl");
const router = express.Router();

router.post("/", createProduct);

router.get("/:id", getAProduct);
router.put("/:id", updateProduct);
router.get("/", getAllProduct);


module.exports = router;