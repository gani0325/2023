const bcrypt = require("bcryptjs");
const UserModel = require("../models/User");

//=================== Routes
// Landing Page
exports.landing_page = (req, res) => {
  res.render("landing");
};

// // Login Page
exports.login_get = (req, res) => {
  res.render("login");
};

exports.login_post = async (req, res) => {
  const { email, password } = req.body;
  const user = await UserModel.findOne({ email });

  // 가입되지 않은 사용자라면
  if (!user) {
    return res.redirect("/login");
  }

  // 비밀번호가 틀렸다면
  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) {
    return res.redirect("/login");
  }

  req.session.isAuth = true;
  res.redirect("/dashboard");
};

// // Register Page
exports.register_get = (req, res) => {
  res.render("register");
};
exports.register_post = async (req, res) => {
  const { username, email, password } = req.body;

  let user = await UserModel.findOne({ email });

  if (user) {
    return res.redirect("/register");
  }

  const hashedPsw = await bcrypt.hash(password, 12);

  user = new UserModel({
    username,
    email,
    password: hashedPsw,
  });

  await user.save();
  res.redirect("/login");
};

// // Dashboard Page
exports.dashboard_get = (req, res) => {
  res.render("dashboard");
};

// // Logout Page
exports.logout_page = (req, res) => {
  req.session.destroy((err) => {
    if (err) throw err;
    res.redirect("/login");
  });
};
