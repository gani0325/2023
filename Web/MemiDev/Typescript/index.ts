// buffer 알아보기
import {Buffer} from "node:buffer";
const arr = [];

arr.push(1);
arr.push(3);
arr.push(5);
arr.push(7);
console.log(arr);       // [ 1, 3, 5, 7 ]

const a = Buffer.from([2, 3, 4, 5]);
console.log(a, a.length);       // <Buffer 02 03 04 05> 4
const b = Buffer.alloc(10);
console.log(b, b.length);       // <Buffer 00 00 00 00 00 00 00 00 00 00> 10
const c = Buffer.allocUnsafe(10)
console.log(c, c.length)        // <Buffer f0 0f f6 05 00 00 00 00 08 59> 10