const express = require("express");
const colors = require("colors");
const dotenv = require("dotenv");

// configure env
dotenv.config();

// rest object
const app = express();

// rest api
app.get("/", (req, res) => {
  res.send("<h>Welcome ecommerce app</h>");
});

// PORT
const PORT = process.env.PORT || 8000;

// run listen
app.listen(PORT, () => {
  console.log(
    `Server Running on ${process.env.DEV_MODE} http://localhost:${PORT}`
  );
});
