const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const crypto = require("crypto");

const UserSchema = new mongoose.Schema({
  firstname: {
    type: String,
    required: true
  },
  lastname: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true,
    unique: true
  },
  mobile: {
    type: String,
    required: true,
    unique: true
  },
  password: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    default: "user",
  },
  isBlocked: {
    type: Boolean,
    default: false,
  },
  cart: {
    type: Array,
    default: [],
  },
  address: {
    type: String
  },
  wishList: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: "Product"
  }],
  refreshToken: {
    type: String,
  },
  passwordChangedAt: Date,
  passwordResetToken: String,
  passwordResetExpires: Date
}, {
  timestamps: true,
  collection: 'users'
});

UserSchema.pre("save", async function (next) {
  if (!this.isModified("password")) {
    next();
  }
  // Create a new User
  // 1) 우선 비밀번호 해쉬화(암호화)
  this.password = await bcrypt.hash(this.password, 12);
  this.passwordConfirm = undefined;
  next();
});

// 비밀번호 재수정 날짜
UserSchema.pre('save', function (next) {
  if (!this.isModified('password') || this.isNew) return next();
  this.passwordChangedAt = Date.now() - 1000;
  next();
});

// check password matching
UserSchema.methods.isPasswordMatched = async function (enteredPassword) {
  return await bcrypt.compare(enteredPassword, this.password);
};

// return JSON Web Token
UserSchema.methods.createPasswordResetToken = function () {
  // Generate Token
  const resetToken = crypto.randomBytes(32).toString("hex");

  // Hash token
  this.passwordResetToken = crypto
    .createHash("sha256")
    .update(resetToken)
    .digest("hex");

  // set expired time
  this.passwordResetExpires = Date.now() + 30 * 60 * 1000   // 10분
  return resetToken;
};

const User = mongoose.model("User", UserSchema);
module.exports = User;