const User = require("../models/User");
const bcrypt = require("bcrypt");
const asyncHandler = require("express-async-handler");

const createUser = asyncHandler(async (req, res) => {
  const { firstname, lastname, email, mobile, password } = req.body;
  const findUser = await User.findOne({ email: email });

  // email이 db에 없다면
  if (!findUser) {
    // Create a new User
    // 1) 우선 비밀번호 해쉬화(암호화)
    const hashedPassword = await bcrypt.hash(password, 10);
    // 2) 새 User 정보 만들기
    const newUser = await User.create({
      firstname, lastname, email, mobile, password: hashedPassword
    });

    res.json(newUser);
  } else {
    // User already exists
    throw new Error("User already exists");
  }
});

const loginCheck = asyncHandler(async (req, res) => {
  const { email, password } = req.body;
  // check if user exists or not
  const findUser = await User.findOne({ email: email });

  // user 가 없다면 done
  if (!findUser) {
    throw new Error("That email is not registered!");
  }
  // Match password (기존 비밀번호와 입력한 비밀번호 체크)
  bcrypt.compare(password, findUser.password, (err, isMatch) => {
    if (err) throw err;
    if (isMatch) {
      res.json(findUser);
    } else {
      throw new Error("Email or Password is incorrect!");
    }
  });
})

module.exports = {
  createUser,
  loginCheck
};