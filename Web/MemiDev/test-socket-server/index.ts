import express from "express"
import birds from "./routes/birds"
import dogs from "./routes/dogs"
const app = express()

app.use("/birds", birds)
app.use("/dogs", dogs)

app.listen(4000)