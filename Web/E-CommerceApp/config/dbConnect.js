const mongoose = require("mongoose");
require("dotenv").config();

// DB config
const db = process.env.MONGODB_URI;
// connect to Mongo
const dbConnect = () => {
  try {
    mongoose.connect(db, {
      useNewUrlParser: true,    // useNewUrlParser : 에러 방지
      useUnifiedTopology: true
    })
    console.log("💚 MongoDB Connected...");
  } catch (error) {
    console.log("❌ MongoDB not Connected...");
  }
};

module.exports = dbConnect;