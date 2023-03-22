const User = require("../models/User");
const bcrypt = require("bcrypt");
const asyncHandler = require("express-async-handler");
const { generateToken } = require("../config/jwtToken");
const { validateMongodbID } = require("../utils/validateMongodbID");

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
})

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
      message : "User unblocked"
    });
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
  unblockUser
};