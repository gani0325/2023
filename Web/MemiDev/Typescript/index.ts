import fs from "node:fs";

class Parent {
    constructor (
        public pName : string,
        private pAge : number
    ) {}
};
class Studnet extends Parent{
    name:string
    age:number
    constructor (name:string, age:number) {
        super("father", 100);
        this.name = name; this.age = age
    };
    get nameAge() {
        return this.name + "-" + this.age
    }
    set nameAge (text:String) {
        const ts = text.split("-");
        if (ts.length < 2) return
        this.name = ts[0];
        this.age = Number(ts[1]);
    }
};
const t = new Studnet("gani", 24);
console.log(t);              // Studnet { name: 'gani', age: 24 }
console.log(t.nameAge);      // gani-24
t.nameAge = "changeGANI-25";
console.log(t)               // Studnet { name: 'changeGANI', age: 25 }