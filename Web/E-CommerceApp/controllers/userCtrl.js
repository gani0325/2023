const User = require("../models/User");
const bcrypt = require("bcrypt");
const asyncHandler = require("express-async-handler");
const { generateToken } = require("../config/jwtToken");
const { validateMongodbID } = require("../utils/validateMongodbID");
const { generateRefreshToken } = require("../config/refreshToken");
const jwt = require("jsonwebtoken");
const crypto = require("crypto");
const { sendEmail } = require("../controllers/emailCtrl");

// create a user
const createUser = asyncHandler(async (req, res) => {
  const email = req.body.email;
  const findUser = await User.findOne({ email: email });
  console.log(findUser)
  // email이 db에 없다면
  if (!findUser) {
    // 새 User 정보 만들기
    const newUser = await User.create(req.body);
    console.log(newUser);
    res.json(newUser);
  } else {
    // User already exists
    throw new Error("User already exists");
  }
});

// login a user
const loginCheck = asyncHandler(async (req, res) => {
  const { email, password } = req.body;
  // check if user exists or not
  const findUser = await User.findOne({ email: email });

  // user 가 없다면 done
  if (!findUser) {
    throw new Error("That email is not registered!");
  }
  // Match password (기존 비밀번호와 입력한 비밀번호 체크)
  bcrypt.compare(password, findUser.password, async (err, isMatch) => {
    const refreshToken = await generateRefreshToken(findUser?._id);
    const updateUser = await User.findByIdAndUpdate(
      findUser._id, {
      refreshToken: refreshToken,
    }, {
      new: true
    }
    );
    res.cookie("refreshToken", refreshToken, {
      httpOnly: true,               // 웹 서버를 통해서만 cookie에 접근
      maxAge: 72 * 60 * 60 * 1000,  // 현재 시간으로부터 만료 시간을 밀리초(millisecond) 단위로 설정
    });

    if (isMatch) {
      res.json({
        _id: findUser?._id,
        firstname: findUser?.firstname,
        lastname: findUser?.lastname,
        email: findUser?.email,
        mobile: findUser?.mobile,
        token: generateToken(findUser?._id)
      });
    } else {
      throw new Error("Email or Password is incorrect!");
    }
  });
});

// Handle refresh token
const handleRefreshToken = asyncHandler(async (req, res) => {
  try {
    const cookie = req.cookies;
    // refresh token 없음!
    if (!cookie?.refreshToken) {
      throw new Error("No Refresh Token in cookies");
    }
    // refresh token 생성!
    const refreshToken = cookie.refreshToken;
    const user = await User.findOne({ refreshToken });

    if (!user) {
      throw new Error("No Refresh token present in db or not matched");
    }
    // refresh token을 secret key 기반으로 생성
    jwt.verify(refreshToken, process.env.SECRET, (err, decoded) => {
      if (err || user.id !== decoded.id) {
        throw new Error("There is something wrong with refresh token");
      }
      // access Token 발급
      const accessToken = generateToken(user?._id);
      res.json({ accessToken });
    });
  } catch (error) {
    throw new Error(error);
  }
});

// logout
const logout = asyncHandler(async (req, res) => {
  const cookie = req.cookies;
  // refresh token 없음!
  if (!cookie?.refreshToken) {
    throw new Error("No Refresh Token in cookies");
  }
  const refreshToken = cookie.refreshToken;
  const user = await User.findOne({ refreshToken });
  if (!user) {
    res.clearCookie("refreshToken", {
      httpOnly: true,  // 웹 서버를 통해서만 cookie에 접근
      secure: true,    // HTTPS에서만 cookie를 사용
    });
    return res.sendStatus(204);   // forbidden
  }
  // token 삭제
  await User.findOneAndUpdate(refreshToken, {
    refreshToken: "",
  });
  // 쿠키 삭제
  res.clearCookie("refreshToken", {
    httpOnly: true,  // 웹 서버를 통해서만 cookie에 접근
    secure: true,    // HTTPS에서만 cookie를 사용
  });
  return res.sendStatus(204)    // forbidden
});

// Update a user
const updateUser = asyncHandler(async (req, res) => {
  const { _id } = req.user;
  validateMongodbID(_id);

  try {
    const updateUser = await User.findByIdAndUpdate(
      _id,
      {
        firstname: req?.body?.firstname,
        lastname: req?.body?.lastname,
        email: req?.body?.email,
        mobile: req?.body?.mobile,
      }, {
      new: true,
    }
    );
    res.json(updateUser);
  } catch (error) {
    throw new Error(error);
  }
});

// get all users
const getAllUsers = asyncHandler(async (req, res) => {
  try {
    const getUser = await User.find();
    res.json({ getUser });
  } catch (error) {
    throw new Error(error);
  }
});

// get a single users
const getAUsers = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);

  try {
    const getUser = await User.findById(id);
    res.json({ getUser });
  } catch (error) {
    throw new Error(error);
  }
});

// delete a user
const deleteAUser = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);

  try {
    const deleteAUser = await User.findByIdAndDelete(id);
    res.json({ deleteAUser });
  } catch (error) {
    throw new Error(error);
  }
});

// block user
const blockUser = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);

  try {
    const block = await User.findByIdAndUpdate(
      id,
      {
        isBlocked: true,
      },
      {
        new: true,
      }
    );
    res.json(block);
    // res.json({
    //   message : "User blocked"
    // });
  } catch (error) {
    throw new Error(error);
  }
});

const unblockUser = asyncHandler(async (req, res) => {
  const { id } = req.params;
  validateMongodbID(id);

  try {
    const unblock = await User.findByIdAndUpdate(
      id,
      {
        isBlocked: false,
      },
      {
        new: true,
      }
    );
    res.json({
      message: "User unblocked"
    });
  } catch (error) {
    throw new Error(error);
  }
});

// 비밀번호 재생성
const updatePassword = asyncHandler(async (req, res) => {
  const { _id } = req.user;
  const { password } = req.body;
  validateMongodbID(_id);
  const user = await User.findById(_id);

  if (password) {
    user.password = password;
    const updatePassword = await user.save();
    res.json(updatePassword);
  } else {
    res.json(user);
  }
});

// 비밀번호 찾기
const forgotPasswordToken = asyncHandler(async (req, res) => {
  const { email } = req.body;
  const user = await User.findOne({ email });

  // 사용자가 없다면
  if (!user) {
    throw new Error("User not found with this email");
  }

  try {
    // user schema 에서 다시 토큰 재발급
    const token = await user.createPasswordResetToken();
    await user.save();

    const resetURL = `Plz, follow this link to reset your password! This is vaild till 10 minutes. <a href='http://localhost:3000/api/user/reset-password/${token}'>Click here</>`
    const data = {
      to: email,
      text: "Hi User!",
      subject: "Forgot password link",
      html: resetURL
    }
    sendEmail(data);
    res.json(token);
  } catch (error) {
    throw new Error(error);
  }
});

module.exports = {
  createUser,
  loginCheck,
  getAllUsers,
  getAUsers,
  deleteAUser,
  updateUser,
  blockUser,
  unblockUser,
  handleRefreshToken,
  logout,
  updatePassword,
  forgotPasswordToken
};