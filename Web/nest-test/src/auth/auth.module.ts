import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UserRepository } from './user.repository';
import { AuthController } from './auth.controller';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';

@Module({
  imports: [
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
  providers: [AuthService]
})
export class AuthModule {}
