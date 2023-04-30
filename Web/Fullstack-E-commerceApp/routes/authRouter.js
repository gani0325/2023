import express from "express";

// router object
const router = express.Router();
import {
  registerController,
  loginController,
  testController,
} from "../controllers/authController.js";
import { requireSignIn, isAdmin } from "../middlewares/authMiddleware.js";

// routing
// REGISTER || METHOD POST
router.post("/register", registerController);

// LOGIN || POST
router.post("/login", loginController);

// test routes
router.get("/test", requireSignIn, isAdmin, testController);

export default router;
