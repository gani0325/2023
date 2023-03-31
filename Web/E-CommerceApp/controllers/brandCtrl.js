const Brand = require("../models/Brand");
const asyncHandler = require("express-async-handler");
const { validateMongodbID } = require("../utils/validateMongodbID");

// 브랜드 생성하기
const createBrand = asyncHandler(async (req, res) => {
  try {
    const newBrand = await Brand.create(req.body);
    res.json(newBrand);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 브랜드 수정하기
const updateBrand = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const updateBrand = await Brand.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    res.json(updateBrand);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 브랜드 삭제하기
const deleteBrand = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const deleteBrand = await Brand.findByIdAndDelete(id);
    res.json(deleteBrand);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 브랜드 조회하기
const getaBrand = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);
  try {
    const getaBrand = await Brand.findById(id);
    res.json(getaBrand);
  }
  catch (error) {
    throw new Error(error);
  }
});

// 모든 브랜드 조회하기
const getallBrand = asyncHandler(async (req, res) => {
  try {
    const getallBrand = await Brand.find();
    res.json(getallBrand);
  }
  catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createBrand,
  updateBrand,
  deleteBrand,
  getaBrand,
  getallBrand,

}