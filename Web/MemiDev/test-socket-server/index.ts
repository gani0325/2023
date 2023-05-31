import express from "express"
import birds from "./routes/birds"
import dogs from "./routes/dogs"
import fs from "node:fs/promises"
const app = express()

app.use("/", express.static("public"))
app.use("/birds", birds)
app.use("/dogs", dogs)
app.use("/", async (req, res) => {
  const b = await fs.readFile("./html/index.html")
  res.send(b.toString())
})
app.listen(4000)