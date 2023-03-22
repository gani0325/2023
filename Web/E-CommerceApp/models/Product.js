const mongoose = require("mongoose");

const ProductSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true,
  },
  slug: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
  },
  description: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
  },
  category: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Category",
  },
  brand: {
    type: String,
    enum: ["Apple", "Samsung", "Lenovo"],
  },
  quantity: {
    type: Number,
    required : true,
  },
  sold: {
    type: Number,
    default: 0,
  },
  images: {
    type: Array,
  },
  color: {
    type: String,
    enum: ["Black", "Brown", "Red"],
  },
  ratings: [{
    star: Number,
    postedby: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
  }]
}, {
  timestamps: true,
  collection: 'product'
});

const Product = mongoose.model("Product", ProductSchema);
module.exports = Product;