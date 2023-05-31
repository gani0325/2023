import express from "express"
import birds from "./routes/birds"
import dogs from "./routes/dogs"
import fs from "node:fs/promises"
const app = express()

app.use("/", express.static("public"))
app.use("/birds", birds)
app.use("/dogs", dogs)

app.listen(4000)