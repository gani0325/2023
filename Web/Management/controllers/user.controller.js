// 비밀번호를 암호화해서 저장하기
const bcryptjs = require("bcryptjs");
const userSesrvice = require("../services/user.services");

exports.register = (rep, res, next) => {
    const {password} = req.body;
    // 솔트 + 비밀번호를 해시로 암호화
    const salt = bcryptjs.genSalt(10);
    // 비동기 방식 파라미터, 암호화에 사용되는 Salt
    req.body.password = bcryptjs.hashSync(password, salt);

    userSesrvice.register(req.bdy, (error, result) => {
        if(error) {
            return next(error);
        }
        return res.status(200).send({
            message : "Success",
            data : result,
        });
    });
};

exports.login = (req, res, next) => {
    const { username, password } = req.body;

    userSesrvice.login({ username, password }, (error, result) => {
        if(error) {
            return next(error);
        }
        return res.status(200).send({
            message : "Success",
            data : result,
        });
    })
}

exports.userProfile = (req, res, next) => {
    return res.status(200).json({ message : "Authorized USER!" });
};