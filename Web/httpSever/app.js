const express = require("express");
const app = express();
require("dotenv").config();

app.set("port", process.env.PORT || 3000);

app.get("/", (req, res) => {
    res.send("Hello express");
});
app.listen(app.get("port"), () => {
    console.log(app.get("port"), "빈 포트에서 대기중");
});