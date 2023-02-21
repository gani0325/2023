"use strict";
const { response } = require("../../app");
const UserSchema = require("./UserSchema");

class User {
    constructor(body) {
        this.body = body;
    }

    async login() {
        const client = this.body;
        try {
            // 클라이언트의 id에 해당하는 object 전달하는 메소드
            const {id, pw} = await UserSchema.getUsersInfo(client.id);
            // await : promise를 반환하기 때문에 .then()으로 접근하여 데이터 가져옴
            
            if (id) {
                // id가 있고, id가 받아온 값과 같다면
                if (id === client.id && pw === client.pw) {
                    return {success : true};
                }
                return {success : false, msg : "비밀번호 틀렸습니다."};
            }
            return {success : false, msg : "존재하지 않는 비밀번호입니다"};
        } catch (err) {
            return { success : false, err };
        }

    }

    async register() {
        const client = this.body;
        try {
            // 데이터 저장하기
          const response = await UserSchema.save(client);
          return response;
        } catch(err) {
          return { success : false, err };
        }
    }
}

// 꼭 밖으로 호출하기
module.exports = User;


// User 로그인 하고, response를 controller가 json으로 처리하도록
// User 안에서 schema 처리?
// => const user = new usrs(req.body);