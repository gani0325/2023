"use strict";
// DOM
// Document Object Model
// 자바스크립트에서 html의 존재하는 데이터들을 가져와서 제어하기
const user_id = document.querySelector("#user_id");      // 선택자 -> HTML의 태그들!!
const user_pw = document.querySelector("#user_pw");
const loginBtn = document.querySelector("button");

console.log(user_id);
console.log("hello");

loginBtn.addEventListener("click", login);

function login() {
    const req = {
        id : user_id.value,
        pw : user_pw.value
    };
    console.log(req);
}