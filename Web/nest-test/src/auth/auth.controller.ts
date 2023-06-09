import { Body, Controller, Post, Req, UseGuards, ValidationPipe } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthCredentialsDto } from './dto/auth-credential.dto';
import { AuthGuard } from '@nestjs/passport';

@Controller('auth')
export class AuthController {
    constructor( private authService: AuthService) {}
    
    // localhost:3000/auth/signUp
    @Post("/signup")
    // ValidationPipe : 요청이 컨트롤러에 있는 핸들러로 들어왔을 때 Dto 에 있는 유효성 조건에 맞게 체크
    signUp(@Body(ValidationPipe) authCredentialsDto: AuthCredentialsDto): Promise<void> {
        return this.authService.signUp(authCredentialsDto);
    }
    
    // 로그인 기능 구현하기
    @Post("/signin")
    signIn(@Body(ValidationPipe) authCredentialsDto: AuthCredentialsDto): Promise<{accessToken: string}> {
        return this.authService.signIn(authCredentialsDto);
    }

    // TEST
    @Post("/authTest")
    // 인증 미들웨어
    // 지정된 경로로 통과할 수 있는 사람과 허용하지 않는 사람을 서버에 알려줌
    @UseGuards(AuthGuard())
    test(@Req() req) {
        console.log("req ", req);
    }

}
