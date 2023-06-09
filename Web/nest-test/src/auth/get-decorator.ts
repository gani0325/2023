import { ExecutionContext, createParamDecorator } from "@nestjs/common";
import { User } from "./user.entity";

// 커스텀 데코레이터 생성함
// req.user 가 아닌 user 파라마티로 바로 유저 객체 갖고 오기
export const GetUser = createParamDecorator((data, ctx: ExecutionContext): User => {
    const req = ctx.switchToHttp().getRequest();
    return req.user;

})