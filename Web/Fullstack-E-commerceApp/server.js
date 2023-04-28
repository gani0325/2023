import express from "express";
import colors from "colors";
import dotenv from "dotenv";
import morgan from "morgan";
import connectDB from "./config/db.js";

// router
import authRouter from "./routes/authRouter.js";

// configure env
dotenv.config();

// Databse config
connectDB();

// rest object
const app = express();

// middlewares
app.use(express.json());
app.use(morgan("dev"));

// routes
app.use("/api/v1/auth", authRouter);

// rest api
app.get("/", (req, res) => {
  res.send("<h>Welcome ecommerce app</h>");
});

// PORT
const PORT = process.env.PORT || 8000;

// run listen
app.listen(PORT, () => {
  console.log(
    `Server Running on ${process.env.DEV_MODE} http://localhost:${PORT}`.bgCyan
      .white
  );
});
