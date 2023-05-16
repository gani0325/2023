import express from "express";
import {
  createProductController,
  deleteProductController,
  getProductController,
  getsingleProductController,
  photoProductController,
  updateProductController,
} from "../controllers/productController.js";
import { isAdmin, requireSignIn } from "../middlewares/authMiddleware.js";
import formidable from "express-formidable";

// router object
const router = express.Router();

// routing
// create category
router.post(
  "/create-product",
  requireSignIn,
  isAdmin,
  formidable(),
  createProductController
);

// getAll Products
router.get("/get-products", getProductController);

// single Product
router.get("/get-product/:slug", getsingleProductController);

// get photo Product
router.get("/get-photo/:pid", photoProductController);

// delete Product
router.delete(
  "/delete-product/:pid",
  requireSignIn,
  isAdmin,
  deleteProductController
);

// update Product
router.put(
  "/update-product/:pid",
  requireSignIn,
  isAdmin,
  formidable(),
  updateProductController
);

export default router;
