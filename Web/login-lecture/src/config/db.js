const mysql = require("mysql");

const db = mysql.createConnection({
    host : "login-lecture.c0wqopjtk4sg.ap-northeast-2.rds.amazonaws.com",
    user : "admin",
    password : "hilee5868",
    database : "login_lecture",
});

db.connect();

module.exports = db;