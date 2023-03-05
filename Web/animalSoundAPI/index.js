const express = require('express')
const app = express()
var cors = require('cors')
const port = 3000

app.use(cors())

// HTTP메소드("라우팅", () => {} 콜백함수)
app.get('/', function (req, res) {
  res.send('Hello World')
})

app.get('/sound/:name', function (req, res) {
  const { name } = req.params;     // params의 key를 {} 넣으면 바로 적용됨
  console.log(name);
  if (name == "dog") {
    res.json({"sound" : "멍멍"})
  } else {
    res.json({"sound" : "알수 없는 울음소리"})
  }
})

app.listen(port, () => {
  console.log(`app listening on ${port}`);
})