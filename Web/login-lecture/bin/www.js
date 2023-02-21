"use strict";

// app.js 부르기
const app = require("../app");
const PORT = process.env.PORT || 3000;      // or

app.listen(PORT, () => {
    console.log("서버 가동");
});