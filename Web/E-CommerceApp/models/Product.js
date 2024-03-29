const mongoose = require("mongoose");

const ProductSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true,
  },
  slug: {
    type: String,
    // unique: true,
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
    type: String,
    required: true,
  },
  brand: {
    type: String,
    // enum: ["Apple", "Samsung", "Lenovo"],
    required: true,
  },
  quantity: {
    type: Number,
    required: true,
  },
  sold: {
    type: Number,
    default: 0,
  },
  images: [],
  color: {
    type: String,
    enum: ["Black", "Brown", "Red", "Pink"],
  },
  ratings: [{
    star: Number,
    comment : String,
    postedby: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
  }],
  totalrating: {
    type: String,
    default: 0,
  },
}, {
  timestamps: true,
  collection: 'product'
});

const Product = mongoose.model("Product", ProductSchema);
module.exports = Product;