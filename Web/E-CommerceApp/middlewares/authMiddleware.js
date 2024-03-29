const User = require("../models/User");
const jwt = require("jsonwebtoken");
const asyncHandler = require("express-async-handler");

const authMiddleware = asyncHandler(async (req, res, next) => {
  let token;
  if (req?.headers?.authorization?.startsWith("Bearer")) {
    token = req.headers.authorization.split(" ")[1];
    try {
      if (token) {
        const decoded = jwt.verify(token, process.env.SECRET);
        const user = await User.findById(decoded?.id);
        req.user = user;
        next();
      }
    } catch (error) {
      throw new Error("Not authorized token expired. Plz login again!");
    }
  } else {
    throw new Error("No token attached to header!");
  }
});

const isAdmin = asyncHandler(async (req, res, next) => {
  const {email} = req.user;
  const adminUser = await User.findOne({email});

  // 관리자인지 사용자인지 확인하기
  if (adminUser.role !== "admin") {
    throw new Error ("You are not an admin!!");
  } else {
    next();
  }
});

module.exports = {
  authMiddleware,
  isAdmin
};