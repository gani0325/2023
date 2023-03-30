const mongoose = require("mongoose");

const categorySchema = new mongoose.Schema({
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

const Category = mongoose.model("Category", categorySchema);
module.exports = Category;