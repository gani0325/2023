// 간단한 변수 타입지정 가능
var 이름 = "gani";
var 사람 = ["kim", "lee"];
var 사람들 = { name: "park" };
// 다양한 타입 -> Union Type
var 이름2 = 123;
// 함수에 타입 지정 가능
function temp(x) {
    return x * 2;
}
var john = [123, true];
var john2 = { name: "kim", age: "24" };
// class 타입 지정
var User = /** @class */ (function () {
    function User(name) {
        this.name = name;
    }
    return User;
}());
