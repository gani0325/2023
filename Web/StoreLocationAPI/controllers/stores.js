const Store = require("../models/Store");

// @desc GET all stores
// @route GET /api/v1/stores
// @access Public
exports.getStores = async (req, res, next) => {
  try {
    const stores = await Store.find();

    return res.status(200).json({
      success: true,
      count: stores.length,
      data: stores,
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error" });
  }
};

// @desc CREATE a stores
// @route POST /api/v1/stores
// @access Public
exports.addStore = async (req, res, next) => {
  try {
    // { storeId: '0001', address: '10 main st' }
    const store = await Store.create(req.body);

    return res.status(200).json({
      success: true,
      data: store,
    });
  } catch (err) {
    console.error(err);
    if (err.code === 11000) {
      return res.status(400).json({ error: "This store already exists" });
    }
    res.status(500).json({ error: "Server error" });
  }
};
