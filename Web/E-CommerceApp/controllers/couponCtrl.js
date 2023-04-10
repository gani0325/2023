const Coupon = require("../models/Coupon");
const asyncHandler = require("express-async-handler");
const { validateMongodbID } = require("../utils/validateMongodbID");

// 쿠폰 생성하기
const createCoupon = asyncHandler(async (req, res) => {
  try {
    const newCoupon = await Coupon.create(req.body);
    res.json(newCoupon);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 쿠폰 수정하기
const updateCoupon = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const updateCoupon = await Coupon.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    res.json(updateCoupon);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 쿠폰 삭제하기
const deleteCoupon = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const deleteCoupon = await Coupon.findByIdAndDelete(id);
    res.json(deleteCoupon);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 쿠폰 조회하기
const getaCoupon = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const getaCoupon = await Coupon.findById(id);
    res.json(getaCoupon);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 모든 쿠폰 조회하기
const getallCoupon = asyncHandler(async (req, res) => {
  try {
    const getallCoupon = await Coupon.find();
    res.json(getallCoupon);
  }
  catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createCoupon,
  updateCoupon,
  deleteCoupon,
  getaCoupon,
  getallCoupon,

}