const express = require('express')
const app = express()
const port = 3000

// HTTP메소드("라우팅", () => {} 콜백함수)
app.get('/', function (req, res) {
  res.send('Hello World')
})

app.get('/user/:id', function (req, res) {
  // 1) get의 params -> q가 id임, :뒤
  const p = req.params
  console.log(p)
  // 2) get의 query -> ?사용한후 뒤에 key value 사용! -> /id?q=~~&name=~~ { q: 'hi', name: 'gani' }
  const q = req.query
  console.log(q)

  res.json({"sound" : "멍멍"})
})

app.get('/cat', function (req, res) {
  res.send({"sound" : "야옹"})
})

app.listen(port, () => {
  console.log(`app listening on ${port}`);
})