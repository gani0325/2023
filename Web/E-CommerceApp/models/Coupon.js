const mongoose = require("mongoose");

const CouponSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true,
    uppercase: true
  },
  expiry: {
    type: Date,
    required: true
  },
  discount: {
    type: Number,
    required: true,
  }
}, {
  timestamps: true,
  collection: 'coupon'
});

const Coupon = mongoose.model("Coupon", CouponSchema);
module.exports = Coupon;