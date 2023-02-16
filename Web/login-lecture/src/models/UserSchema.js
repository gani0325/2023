"use strict";

class UserSchema{
    // 밑은 원래 db로 받아오는겨
    static #users = {
        id : ["gani", "gaeun"],
        pw : ["1234", "2334"],
        name : ["가니", "가은", "간"]
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
}

module.exports = UserSchema;
