const express = require("express");
const router = express.Router();
const { createUser, loginCheck, getAllUsers, getAUsers, deleteAUser, updateUser, blockUser, unblockUser } = require("../controllers/userCtrl");
const { authMiddleware, isAdmin } = require("../middlewares/authMiddleware");

router.post("/register", createUser);
router.post("/login", loginCheck);

router.get("/all-users", getAllUsers);
router.get("/:id", authMiddleware, isAdmin, getAUsers);
router.delete("/:id", deleteAUser);
router.put("/edit-user", authMiddleware, updateUser);
router.put("/block-user/:id", authMiddleware, isAdmin, blockUser);
router.put("/unblock-user/:id", authMiddleware, isAdmin, unblockUser);

module.exports = router;