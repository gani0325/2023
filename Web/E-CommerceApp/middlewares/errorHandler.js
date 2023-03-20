// not found
const notFound = (req, res, next) => {
  const error = new Error(`Not Found : ${req.originalUrl}`);
  res.status(404);
  next(error);
};

// Error Handler
// - 1xx
// : 요청을 받았으며 프로세스 계속 진행
// - 2xx
// : 요청을 성공적으로 받았으며 인식했고 수용
// - 3xx
// : 요청 완료를 위해 추가 작업 조치 필요 
// - 4xx
// : 요청의 문법이 잘못되었거나 요청 처리 불가능
// - 5xx
// : 서버가 명백히 유효한 요청에 대해 충족을 실패 
const errorHandler = (err, req, res, next) => {
  const statuscode = res.statusCode == 200 ? 500 : res.statusCode;
  res.status(statuscode);
  res.json({
    message: err?.message,
    stack: err?.stack
  });
};

module.exports = {
  notFound,
  errorHandler
};