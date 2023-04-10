const express = require("express");
const { createProduct, getAProduct, getAllProduct, updateProduct, deleteProduct, addTowishList, rating, uploadImages } = require("../controllers/productCtrl");
const { isAdmin, authMiddleware } = require("../middlewares/authMiddleware");
const { uploadPhoto, productImgResize } = require("../middlewares/uploadimages");
const router = express.Router();

router.post("/", authMiddleware, isAdmin, createProduct);
router.put("/upload/:id", authMiddleware, isAdmin, uploadPhoto.array("images", 10), productImgResize, uploadImages);
router.get("/:id", getAProduct);
router.put("/wishlist", authMiddleware, addTowishList);
router.put("/rating", authMiddleware, rating);

router.put("/:id", authMiddleware, isAdmin, updateProduct);
router.delete("/:id", authMiddleware, isAdmin, deleteProduct);
router.get("/", getAllProduct);

module.exports = router;