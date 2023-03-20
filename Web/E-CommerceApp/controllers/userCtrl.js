const User = require("../models/User");

const createUser = async (req, res) => {
  const email = req.body.email;
  const findUser = await User.findOne({email : email});

  // email이 db에 없다면
  if (!findUser) {
    // Create
    const newUser = await User.create(req.body);
    res.json(newUser);
  } else {
    // User already existed
    res.json({
      msg: "User already existed!",
      success: false,
    });
  }
};

module.exports = createUser;