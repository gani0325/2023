"use strict";

class UserSchema{
    // 밑은 원래 db로 받아오는겨
    static #users = {
        id : ["gani", "gaeun"],
        pw : ["1234", "2334"],
        name : ["가니", "가은"]
    };

    static getUsers(...fields) {
        const users = this.#users;
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
        const users = this.#users;
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
    
    // 회원가입 임시 저장
    static save(userInfo) {
        const users = this.#users;
        users.id.push(userInfo.id);
        users.pw.push(userInfo.pw);
        users.name.push(userInfo.name);
        return { success : true };
    }
}

module.exports = UserSchema;
