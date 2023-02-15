"use strict";

// app.js 부르기
const app = require("../app");
const PORT = 3000;

app.listen(PORT, () => {
    console.log("서버 가동");
});