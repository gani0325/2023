import http from "node:http"

const server = http.createServer((req, res) => {
  if (req.url === "/about") res.end("good!!")
  else res.end("hello")
})

server.listen(3000)