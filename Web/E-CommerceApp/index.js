const express = require("express");
const dbConnect = require("./config/dbConnect");
const app = express();
require("dotenv").config();
const PORT = process.env.PORT || 8000;

// mongoDB
dbConnect();

app.use("/", (req, res) => {
  res.send("hihi");
})
app.listen(PORT, () => {
    console.log(`🚀 Server started on port http://localhost:${PORT}`);
});