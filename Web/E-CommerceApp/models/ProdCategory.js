const mongoose = require("mongoose");

const prodCategorySchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    unique: true,
    index: true
  },
}, {
  timestamps: true,
  collection: 'category'
});

const Category = mongoose.model("Category", prodCategorySchema);
module.exports = Category;