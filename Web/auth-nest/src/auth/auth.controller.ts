import { Body, Controller, HttpCode, HttpStatus, Post, Req, UseGuards } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthDto } from './dto/auth.dto';
import { Tokens } from './types';
import { AuthGuard } from '@nestjs/passport';

@Controller('auth')
export class AuthController {
    constructor(private authService: AuthService) {}
    
    @Post("/local/signup")
    @HttpCode(HttpStatus.CREATED)
    signupLocal(@Body() dto: AuthDto): Promise<Tokens> {
      return this.authService.signupLocal(dto);
    }

    @Post("/local/signin")
    @HttpCode(HttpStatus.OK)
    signinLocal(@Body() dto: AuthDto): Promise<Tokens> {
      return this.authService.signinLocal(dto);
    }


    @UseGuards(AuthGuard("jwt"))
    @Post("/logout")
    @HttpCode(HttpStatus.OK)
    logout(@Req() req: Request) {
      const user = req.user;
      return this.authService.logout(user["sub"]);
    }

    @UseGuards(AuthGuard("jwt-refresh"))
    @Post("/refresh")
    @HttpCode(HttpStatus.OK)
    refreshTokens(@Req() req: Request) {
      const user = req.user;
      return this.authService.refreshTokens(user["sub"], user["refreshToken"]);
    }
}
