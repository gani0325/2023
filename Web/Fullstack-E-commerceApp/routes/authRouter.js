import express from "express";

// router object
const router = express.Router();
import { registerController } from "../controllers/authController.js";

// routing
// REGISTER || METHOD POST
router.post("/register", registerController);

export default router;
