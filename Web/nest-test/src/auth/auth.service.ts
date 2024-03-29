import { Injectable, UnauthorizedException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { UserRepository } from './user.repository';
import { AuthCredentialsDto } from './dto/auth-credential.dto';
import * as bcrypt from "bcryptjs";
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class AuthService {
    constructor(
        @InjectRepository(UserRepository)
        private userRepository: UserRepository,
        private jwtService: JwtService
    ) {}
    
    // 회원가입
    async signUp(authCredentialsDto: AuthCredentialsDto): Promise<void> {
        return this.userRepository.createUser(authCredentialsDto);
    }

    // 로그인
    async signIn(authCredentialsDto: AuthCredentialsDto): Promise<{accessToken: string}> {
        const {username, password} = authCredentialsDto;
        // 해당 아이디가 데이터베이스에 있는 아이디인지 확인
        const user = await this.userRepository.findOne({username});
        
        // 제공 받은 비밀번호와 있는 아이디의 비밀번호와 비교하기
        if (user && (await bcrypt.comepare(password, user.password))){
            // 로그인 성공 시 유저 토큰 생성 (secret + payload)
            const payload = {username};
            const accessToken = await this.jwtService.sign(payload);

            return { accessToken };
        } else {
            throw new UnauthorizedException("login fail");
        }
    }
}
