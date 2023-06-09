import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UserRepository } from './user.repository';
import { AuthController } from './auth.controller';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { JwtStrategy } from './jwt.strategy';
import { Passport } from 'passport';

@Module({
  imports: [
    // 유저를 인증하기위해 사용할 기본 stragety 명시
    PassportModule.register({ defaultStrategy: "jwt"}),
    JwtModule.register({
      // 토큰을 만들 때 이용하는 Secret 텍스트
      secret: "Secret1234", // 아무거나 해도 됨
      signOptions: {
        // 정해진 시간 이후에는 토큰이 유효하지 않게 됨 (60 * 60 은 한시간)
        expiresIn: 60 * 60,
      }
    }),
    TypeOrmModule.forFeature([UserRepository])
  ],
  controllers: [AuthController],
  // JwtStrategy를 이 Auth 모듈에서 사용할 수 있도록 등록
  providers: [AuthService, JwtStrategy],
  // 다른 곳에서도 사용해야 하므로 exports..
  exports: [JwtStrategy, PassportModule]
})
export class AuthModule {}
