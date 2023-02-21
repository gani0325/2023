const {createLogger, transports, format}= require("winston");
const {combine, timestamp, printf, label, json, simple, colorize} = format;

const printFormat = printf(({timestamp, label, level, message}) => {
    return `${timestamp} [${label}] ${level} : ${message}`;
});

const printLogFormat = combine(
    label({
        label : "백엔드 어렵다"
    }),
    colorize(),
    timestamp({
        format : "YYYY-MM-DD HH:mm:dd",
    }),
    printFormat
)

const logger = createLogger({
    transports : [
        new transports.Console({
            level : "info",
            format : printLogFormat
        }),
    ],
});

module.exports = logger;