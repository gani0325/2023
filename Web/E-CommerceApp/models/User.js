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
  address: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: "Address"
  }],
  wishList: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: "Product"
  }],
  refreshToken: {
    type: String,
  },
  passwordChangedAt : {
    type : Date
  },
  passwordResetToken : {
    type : String
  },
  passwordResetExpires : {
    type : Date
  }
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
  const salt = await bcrypt.genSaltSync(10);
  this.password = await bcrypt.hash(this.password, salt);
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