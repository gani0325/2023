const mongoose = require("mongoose");

const OrderSchema = new mongoose.Schema({
  products: [
    {
      product: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Product",
      },
      count: Number,
      color: String,
    },
  ],
  paymentIntent: {},
  orderStatus: {
    type: String,
    default: "Not Processed",
    enum: ["Not Processed", "Cash on Delivery", "Processing", "Dispatched", "Delivered"],
  },
  orderby: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
  }
}, {
  timestamps: true,
  collection: 'orders'
});


const Order = mongoose.model("Order", OrderSchema);
module.exports = Order;