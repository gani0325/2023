const express = require("express");
const { createCoupon, updateCoupon, deleteCoupon, getaCoupon, getallCoupon } = require("../controllers/couponCtrl");
const { authMiddleware, isAdmin } = require("../middlewares/authMiddleware");
const router = express.Router();

router.post("/", authMiddleware, isAdmin, createCoupon);
router.put("/:id", authMiddleware, isAdmin, updateCoupon);
router.delete("/:id", authMiddleware, isAdmin, deleteCoupon);

router.get("/:id", getaCoupon);
router.get("/", getallCoupon);

module.exports = router;