import { Socket } from "node:dgram"
import net from "node:net"

const client = net.createConnection({port: 3000})

client
  .on("ready", () => {
    console.log("ready")
    client.write("hello?")
  })
  .on("close", () => console.log("close"))
  .on("error", (e) => console.log("err", e))
  .on("data", (d) => {
    console.log(d)
    console.log(d.toString())
  })