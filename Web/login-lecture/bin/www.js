"use strict";

// app.js λΆλ₯΄κΈ°
const app = require("../app");
const logger = require("../src/config/logger");

const PORT = process.env.PORT || 3000;      // or

app.listen(PORT, () => {
    logger.info(`π ${PORT} μμ μλ² κ°λ`);
});