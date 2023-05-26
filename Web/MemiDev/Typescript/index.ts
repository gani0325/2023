import {EventEmitter} from "node:events";

class Studnet extends EventEmitter{
    name:string
    age:number
    private timer: NodeJS.Timer
    constructor (name:string, age:number) {
        super();
        this.name = name;
        this.age = age;
        this.timer = this.timerOn();
    };
    timerOn () {
        return setInterval(() => {
            this.emit("changed", this.nameAge);
        }, 2000);
    }
    timerOff () {
        clearInterval(this.timer);
    }
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
t.on("changed", (a) => {
    console.log(new Date(), a);
});

let count = 0;
setInterval(() => {
    t.nameAge = "aa-" + count++
}, 100);