"use strict";
// DOM
// Document Object Model
// 자바스크립트에서 html의 존재하는 데이터들을 가져와서 제어하기
const user_id = document.querySelector("#user_id");      // 선택자 -> HTML의 태그들!!
const user_pw = document.querySelector("#user_pw");
const loginBtn = document.querySelector("#button");

loginBtn.addEventListener("click", login);

function login() {
    if (!user_id.value) return alert("아이디를 입력하세요.");
    if (!user_pw.value) return alert("비밀번호를 입력하세요.");

    const req = {
        id : user_id.value,
        pw : user_pw.value
    };
    
    // 데이터 전달하는 과정 (ROUTER server에 API 경로 있어야됨)
    fetch("/login", {
        method : "POST",                // 쓰기
        headers : {
            "Content-Type" : "application/json",
        },
        body : JSON.stringify(req),      // json type으로
    })
        .then((res) => res.json())
        .then((res) => {
            // 로그인 성공하면 main으로
            if (res.success) {
                location.href = "/";
            } else {
                if (res.err) return alert(res.err);
                alert(res.msg);
            }
        })
        .catch((err) => {
            console.error(new Error("회원가입 중 에러 발생"));
        });
    // res.json()의 반환값은 promise
    // 기본 res의 반환값은 response 스트림
}