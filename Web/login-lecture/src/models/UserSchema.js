"use strict";
// database 읽어오기
const db= require("../config/db");

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

    static #getUsers(data, isAll, fields) {
        const users = JSON.parse(data);
        if (isAll) return users;

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

    static getUsers(isAll, ...fields) {
    }

    static getUsersInfo(id) {
        return new Promise((resolve, reject) => {
            const query = "SELECT * FROM users WHERE id = ?;";
            db.query(query, [id], (err, data) => {
                if (err) reject(`${err}`);
                else resolve(data[0]);
            });
        });
    }
    
    // 회원가입 임시 저장
    static async save(userInfo) {
        return new Promise((resolve, reject) => {
            const query = "INSERT INTO users(id, name, pw) VALUES(?, ?, ?);";
            db.query(query,
                [userInfo.id, userInfo.name, userInfo.pw], (err) => {
                    if (err) reject(`${err}`);
                    else resolve({ success : true });
            });
        });
    }
}

module.exports = UserSchema;
