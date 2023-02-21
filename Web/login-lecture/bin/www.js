"use strict";

// app.js 부르기
const app = require("../app");
const logger = require("../src/config/logger");

const PORT = process.env.PORT || 3000;      // or

app.listen(PORT, () => {
    logger.info(`🚀 ${PORT} 에서 서버 가동`);
});