"use strict";
// database 읽어오기
const fs = require("fs").promises;
// promises : promise가 수행하는 동작이 끝남과 동시에 상태를 알려주기 때문에 비동기 처리
// pending : 데이터를 전부 읽어오지 못함

class UserSchema{
    static #getUserInfo(data, id) {
        const users = JSON.parse(data);
        const idx = users.id.indexOf(id);
        // users의 키값들만 배열로! [id, pw, name]
        const usersKeys = Object.keys(users);
        // reduce 반복문을 통해 newUser에 키값이 순서대로 들어감
        // users의 키값의 idx(id에 해당하는 값 넣기)
        const userInfo = usersKeys.reduce((newUsers, info) => {
            newUsers[info] = users[info][idx];
            return newUsers;
        }, {});
        return userInfo;
    }

    static getUsers(...fields) {
        // const users = this.#users;
        // reduce : 반복문
        const newUsers = fields.reduce((newUsers, field) => {
            // users에 해당하는 키(field)값이 있으면 오브젝트(newUsers)에 넣어주겠음
            if (users.hasOwnProperty(field)) {
                newUsers[field] = users[field];
            }
            return newUsers;
        }, {});
        return newUsers;
    }

    static getUsersInfo(id) {
        return fs.readFile("./src/databases/user.json")
            .then((data) => {
                return this.#getUserInfo(data, id);
            })
            .catch(console.error);
    }
    
    // 회원가입 임시 저장
    static save(userInfo) {
        // const users = this.#users;
        users.id.push(userInfo.id);
        users.pw.push(userInfo.pw);
        users.name.push(userInfo.name);
        return { success : true };
    }
}

module.exports = UserSchema;
