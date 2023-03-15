class AppError extends Error {
    constructor( description) {
      super(description);
      Error.captureStackTrace(this);
    }
  }
  
  module.exports = AppError;