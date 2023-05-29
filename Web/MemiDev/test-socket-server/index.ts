import net from "node:net"

const server = net.createServer(socket => {
    console.log("greeting")
    socket
      .on("ready", () => console.log("ready"))
      .on("close", () => console.log("close"))
      .on("error", (e) => console.log("err", e))
      .on("data", (d) => {
        console.log(d)
        console.log(d.toString())
        // const req = d.toString()
        // const ps = req.split(" ")
        // console.log(ps)
        socket.write("ok good")
      })
})

server.listen(3000)