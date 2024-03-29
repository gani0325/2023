const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");
const passport = require("passport");
// user model
const User = require("../models/User");

// Login Page
router.get("/login", (req, res) => {
  res.render("login");
});

// Register Page
router.get("/register", (req, res) => {
  res.render("register");
});

// Register Handle
router.post('/register', (req, res) => {
  const { name, email, password, password2 } = req.body;
  let errors = [];

  if (!name || !email || !password || !password2) {
    errors.push({ msg: 'Please enter all fields' });
  }

  if (password != password2) {
    errors.push({ msg: 'Passwords do not match' });
  }

  if (password.length < 6) {
    errors.push({ msg: 'Password must be at least 6 characters' });
  }

  if (errors.length > 0) {
    res.render('register', {
      errors,
      name,
      email,
      password,
      password2
    });
  } else {
    // validation pass
    User.findOne({ email: email })
      .then(user => {
        // email을 찾았는데 만약에 user가 있다면
        if (user) {
          errors.push({ msg: "Email is already registered!" });
          res.render('register', {
            errors,
            name,
            email,
            password,
            password2
          });
        } else {
          // 회원가입된 email이 없다면
          const newUser = new User({
            name,
            email,
            password
          });

          console.log(newUser);

          // hash password
          bcrypt.genSalt(10, (err, salt) =>
            bcrypt.hash(newUser.password, salt, (err, hash) => {
              if (err) throw err;
              // Set password to hased
              newUser.password = hash;
              // save user
              newUser.save()
                .then(user => {
                  req.flash("success_msg", "You are now registered and can log in!!");
                  res.redirect('/users/login');
                })
                .catch(err => console.log(err));
            }))
        }
      });
  }
});

// Login handle
router.post("/login", (req, res, next) => {
  passport.authenticate("local", {
    // 성공하면 메인으로
    successRedirect : "/dashboard",
    // 실패하면 다시 로그인
    failureRedirect : "/users/login",
    failureFlash : true
  }) (req, res, next);
});

// Logout handle
router.get('/logout', (req, res, next) => {
  req.logOut(err => {
    if (err) {
      return next(err);
    } else {
      console.log('로그아웃됨.');
      req.flash("success-msg", "You are logged out!");
      res.redirect("/users/login");
    }
  });
});

module.exports = router;