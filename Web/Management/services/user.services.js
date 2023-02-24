const User = require("../models/user.model");
const bcrypt = require("bcryptjs");
const auth = require("../middlewares/auth.js")

async function login({ username, password }, callback) {
    const user = await User.findOne({ username });

    if (user != null) {
        // client가 입력한 password와 user.passward와 일치한지 확인
        if (bcrypt.compareSync(password, user.password)) {
            // accessToken 생성기 (middleware에서 발행)
            const token = auth.generateAccessToken(username);
            return callback(null, {...user.toJSON(), token});
        }
        else {
            return callback({
                message : "일치하지 않은 아이디와 비밀번호입니다.",
            });
        }
    } else {
        return callback({
            message : "일치하지 않은 아이디와 비밀번호입니다.",
        });
    }
}

async function register(params, callback) {
    if(params.username === undefiend) {
        return callback({message : "아이디 입력해주세요"});
    }

    const user = new User(params);
    user.save()
        .then((response) => {
            return callback(null, response);
        })
        .catch((error) => {
            return callback(error);
        });
}

module.exports = {
    login,
    register,
};