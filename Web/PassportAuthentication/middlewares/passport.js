// 인증 요청을 처리해주는 Node.js의 인증 미들웨어

const LocalStrategy = require("passport-local").Strategy;
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");

// Load user model
const User = require("../models/User");

module.exports = (passport) => {
  passport.use(
    new LocalStrategy({ usernameField: "email" }, (email, password, done) => {
      // Match User
      User.findOne({ email: email })
        .then(user => {
          // user 가 없다면 done
          if (!user) {
            return done(null, false, { message: "That email is not registered!" });
          }
          // Match password (기존 비밀번호와 입력한 비밀번호 체크)
          bcrypt.compare(password, user.password, (err, isMatch) => {
            if (err) throw err;

            if (isMatch) {
              return done(null, user);
            } else {
              return done(null, false, { message: "Email or Password is incorrect!" });
            }
          });
        })
        .catch(err => console.log(err));
    })
  );

  // login이 최초로 성공했을 때만 호출되는 함수
  // done(null, user.id)로 세션을 초기화
  passport.serializeUser(function (user, cb) {
    process.nextTick(function () {
      return cb(null, user);
    });
  });

  // 사용자가 페이지를 방문할 때마다 호출되는 함수
  // done(null, id)로 사용자의 정보를 각 request의 user 변수에 넣음  
  passport.deserializeUser(function (user, cb) {
    process.nextTick(function () {
      return cb(null, user);
    });
  });
}