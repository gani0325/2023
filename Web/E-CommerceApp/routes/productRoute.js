const express = require("express");
const { createProduct, getAProduct, getAllProduct, updateProduct, deleteProduct } = require("../controllers/productCtrl");
const router = express.Router();

router.post("/", createProduct);

router.get("/:id", getAProduct);
router.put("/:id", updateProduct);
router.delete("/:id", deleteProduct);
router.get("/", getAllProduct);


module.exports = router;