"use strict";

const output = {
    home : (req, res) => {
        res.render("home/index");
    },
    
    login : (req, res) => {
        res.render("home/login");
    },
}

const users = {
    id : ["gani", "gaeun"],
    pw : ["1234", "2334"],
};

const process = {
    login : (req, res) => {
        const id = req.body.id;
        const pw = req.body.pw;

        // id가 users.id에 있을경우
        if (users.id.includes(id)) {
            const idx = users.id.indexOf(id);
            if (users.pw[idx] === pw) {
                return res.json({
                    success : true,
                });
            }
        }
        return res.json({
            success : false,
            msg : "로그인에 실패하셨습니다.",
        });
    },
}

// 꼭 밖으로 호출하기
module.exports = {
    output,
    process,
};