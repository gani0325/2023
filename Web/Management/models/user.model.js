const mongoose = require("mongoose");
const {Schema} = mongoose;
// Mongoose 스키마 내의 고유한 필드에 대한 사전 저장 유효성 검사를 추가하는 플러그인
const uniqueValidator = require("mongoose-unique-validator");

const userSchema = new Schema ({
    username : {
        type : String,
        required : true
    },
    email : {
        type : String,
        required : true,
        unique : true
    },
    password : {
        type : String,
        required : true
    },
    date : {
        type : Date,
        default : Date.now()
    }
});

userSchema.set("toJSON", {
    transform : (document, returnedObject) => {
        returnedObject.id = returnedObject._id.toString();
        // _id, _v, password 전역 스키마 설정을 등록하여 삭제
        delete returnedObject._id;
        delete returnedObject._v;
        delete returnedObject.password;
    },
});

// unique의 존재 유무도 파악
userSchema.plugin(uniqueValidator, { message : "Email 이미 사용 중"});

// schema를 사용하는 model
const User = mongoose.model("user", userSchema);
module.exports = User;