const pr = console.log;

let a = [23, 4, 5];
pr(a);
a.push(23);
pr(a);
a.pop();
pr(a);

a.forEach((v) => {
  pr(v);
});
// 23
// 4
// 5

const b = a.map((v) => v + "b");
pr(b);
// [ '23b', '4b', '5b' ]

const c = [];
const d = [1, 2, 3];

d.forEach((v1) => {
  c.push(v1);
});
pr(c);
const e = d.concat(a);

let d1 = new Date(2000, 3, 3);
let d2 = new Date();
pr(d1, d2);
// 2000-04-24T15:00:00.000Z 2023-05-26T07:05:22.893Z

pr(d1.toLocaleDateString());
// 4/3/2000

pr(d1.toLocaleString());
// 4/3/2000, 12:00:00 AM

setTimeout(() => {
  pr("hello");
}, 1000);

// interval은 변수에 넣어 사용하길!
setInterval(() => {
  pr("interval");
}, 1000);

// 블로킹 -> 하나 끝나고 그다음 일 수행함
for (let i = 0; i < 10; i++) {
  setTimeout(() => {
    pr("블로킹 ");
  }, 1000);
  pr("블로킹중");
}

const fs1 = require("fs");
fs1.writeFile("./text.txt", "hello", (err) => {
  if (err) console.error(err.message);
  pr("good");
});

// 비동기
const fs = require("node:fs/promises");
fs.writeFile("./text.txt", "비동기")
  .then(() => {
    pr("w");
  })
  .catch((e) => {
    pr(e.message);
  });
fs.readFile("./text.txt")
  .then((r) => {
    pr(r.toString());
  })
  .catch((e) => {
    pr(e.message);
  })
  .finally(() => {
    pr("final");
  });

// async await
const foo = async () => {
  await fs.writeFile("./text2.txt", "async awiat");
  const r = await fs.readFile("./text2.txt");
  pr(r.toString());
};
foo();
