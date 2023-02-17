"use strict";
const { response } = require("../../app");
const UserSchema = require("./UserSchema");

class User {
    constructor(body) {
        this.body = body;
    }

    login() {
        const client = this.body;
        // 클라이언트의 id에 해당하는 object 전달하는 메소드
        const { id, pw } = UserSchema.getUsersInfo(client.id);
        
        if (id) {
            // id가 있고, id가 받아온 값과 같다면
            if (id === client.id && pw === client.pw) {
                return {success : true};
            }
            return {success : false, msg : "비밀번호 틀렸습니다."};
        }
        return {success : false, msg : "존재하지 않는 비밀번호입니다"};
    }

    register() {
        const client = this.body;
        // 데이터 저장하기
        const response = UserSchema.save(client);
        return response;
    }
}

// 꼭 밖으로 호출하기
module.exports = User;


// User 로그인 하고, response를 controller가 json으로 처리하도록
// User 안에서 schema 처리?
// => const user = new usrs(req.body);