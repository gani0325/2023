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
  collection: 'prodCategory'
});

const prodCategory = mongoose.model("prodCategory", prodCategorySchema);
module.exports = prodCategory;