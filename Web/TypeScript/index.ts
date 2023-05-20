// 간단한 변수 타입지정 가능
let 이름 :string = "gani";
let 사람 :string[] = ["kim", "lee"];
let 사람들 :{name? : string} = {name : "park"}

// 다양한 타입 -> Union Type
let 이름2 :string | number = 123;

// 타입은 변수에 담아쓸 수 있음
type MyTYPE = string | number;

// 함수에 타입 지정 가능
function temp(x : number) {
    return x * 2
}

// array에 쓸 수 있는 tuple 타입
type Member = [number, boolean];
let john:Member = [123, true];

// object에 타입지정해야 할 속성이 많으면
type Member2 = {
    [key:string] : string
}
let john2 : Member2 = {name : "kim", age : "24"}

// class 타입 지정
class User {
    name : string;
    constructor(name: string) {
        this.name = name;
    }
}