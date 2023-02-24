function errorHandler(err, req, res, next) {
    if(typeof err === "string") {
        // 400(잘못된 요청): 서버가 요청의 구문을 인식하지 못했다
        return res.status(400).json({message : err});
    }
    if(typeof err === "ValidationError") {
        return res.status(400).json({message : err.message});
    }
    if(typeof err === "UnauthorizedError") {
        // 401(권한 없음): 이 요청은 인증이 필요
        return res.status(401).json({message : err.message});
    }
    // 500 (내부 서버 오류): 서버에 오류가 발생하여 요청을 수행할 수 없다
    return res.status(500).json({message : err.message});
};

module.exports = {
    errorHandler,
};