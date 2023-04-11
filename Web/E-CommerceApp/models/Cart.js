const mongoose = require("mongoose");

const CartSchema = new mongoose.Schema({
  products: [
    {
      product: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Product",
      },
      count: Number,
      color: String,
      price: Number,
    },
  ],
  cartTotal: Number,
  totalAfterDiscount: Number,
  orderby: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
  }
}, {
  timestamps: true,
  collection: 'orders'
});


const Cart = mongoose.model("Cart", CartSchema);
module.exports = Cart;