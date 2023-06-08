import { Body, Controller, Post, ValidationPipe } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthCredentialsDto } from './dto/auth-credential.dto';

@Controller('auth')
export class AuthController {
    constructor( private authService: AuthService) {}
    
    // localhost:3000/auth/signUp
    @Post("/signup")
    // ValidationPipe : 요청이 컨트롤러에 있는 핸들러로 들어왔을 때 Dto 에 있는 유효성 조건에 맞게 체크
    signUp(@Body(ValidationPipe) authCredentialsDto: AuthCredentialsDto): Promise<void> {
        return this.authService.signUp(authCredentialsDto);
    }
}
