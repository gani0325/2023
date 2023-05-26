// 1
let a: number | string = 3434;
a = "abd"
console.log(a)

// 2
const sum = (a : number, b:number) => a+b;
console.log(sum(4, 5));

// 3
interface Studnet {
    name:string
    age:number
};
const student: Studnet = {
    name : "hi", age: 24
};
const change = (x:Studnet) => {
    x.name ="change"
    x.age = 44
};
console.log(student)