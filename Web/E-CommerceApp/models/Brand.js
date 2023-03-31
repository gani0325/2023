const mongoose = require("mongoose");

const BrandSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    unique: true,
    index: true
  },
}, {
  timestamps: true,
  collection: 'brand'
});

const Brand = mongoose.model("Brand", BrandSchema);
module.exports = Brand;