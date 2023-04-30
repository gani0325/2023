import express from "express";

// router object
const router = express.Router();
import {
  registerController,
  loginController,
  testController,
} from "../controllers/authController.js";

// routing
// REGISTER || METHOD POST
router.post("/register", registerController);

// LOGIN || POST
router.post("/login", loginController);

// test routes
router.get("test", testController);

export default router;
