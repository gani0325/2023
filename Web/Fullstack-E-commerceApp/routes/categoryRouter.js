import express from "express";
import { isAdmin, requireSignIn } from "../middlewares/authMiddleware.js";
import {
  categoryController,
  createCategoryController,
  deleteCategoryController,
  singleCategoryController,
  updateCategoryController,
} from "../controllers/categoryController.js";

// router object
const router = express.Router();

// routing
// create category
router.post(
  "/create-category",
  requireSignIn,
  isAdmin,
  createCategoryController
);

// update category
router.put(
  "/update-category/:id",
  requireSignIn,
  isAdmin,
  updateCategoryController
);

// getAll category
router.get("/get-categories", categoryController);

// single category
router.get("/single-categories/:slug", singleCategoryController);

// delete category
router.delete(
  "/delete-categories/:id",
  requireSignIn,
  isAdmin,
  deleteCategoryController
);

export default router;
