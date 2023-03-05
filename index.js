const express = require('express')
const app = express()

// HTTP메소드("라우팅", () => {} 콜백함수)
app.get('/', function (req, res) {
  res.send('Hello World')
})

app.listen(port, () => {
  console.log(`app listening on ${port}`, port);
})