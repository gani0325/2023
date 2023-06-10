import { Injectable, UnauthorizedException } from "@nestjs/common";
import { PassportStrategy } from "@nestjs/passport";
import { InjectRepository } from "@nestjs/typeorm";
import { ExtractJwt, Strategy } from "passport-jwt";
import { UserRepository } from "./user.repository";
import { User } from "./user.entity";
import * as config from "config";

const jwtConfig = config.get("jwt");

@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
    constructor(
        @InjectRepository(UserRepository)
        private userRepository: UserRepository
    ) {
        super({
            // JWT token in order to validate it
            // Access its payload
            secretOrKey: process.env.JWT_SECRET || jwtConfig.secret,
            // to look for the JWT in the Authorization Header of current Request
            // passed over as a Bearer token
            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken()
        })
    }

    // 토큰이 유효한지 체크가 되면 validate 메소드에서 payload 에 있는 유저 이름이
    // 데이터베이스에서 있는 유저인지 확인! 있다면 유저 객체 return
    // return @UseGuards(AuthGuard()) 이용한 모든 요청의 Request Object에 들어감
    async validate(payload) {
        const {username} = payload;
        const user: User = await this.userRepository.findOne({username});

        if (!user) {
            throw new UnauthorizedException();
        }

        return user;
    }
}
