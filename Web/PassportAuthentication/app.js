const express = require("express");
const app = express();

// Routes
app.use("/", require("./routes/index"));
app.use("/users", require("./routes/user"));

const PORT = process.env.PORT || 8000;

app.listen(PORT, console.log(`🚀Server started on port http://localhost:${PORT}`));