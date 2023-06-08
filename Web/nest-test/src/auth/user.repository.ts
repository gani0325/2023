import { EntityRepository, Repository } from "typeorm";
import { User } from "./user.entity";
import { AuthCredentialsDto } from "./dto/auth-credential.dto";
import { ConflictException, InternalServerErrorException } from "@nestjs/common";
import * as bcrypt from "bcryptjs";
@EntityRepository(User)
export class UserRepository extends Repository<User> {
    async createUser(authCredentialsDto: AuthCredentialsDto): Promise<void> {
        const { username, password } = authCredentialsDto;

        // bcrypt 로 비밀번호를 암호화 한 후 데이터베이스에 저장하기
        const salt = await bcrypt.genSalt();
        const hashedPassword = await bcrypt.hash(password, salt);
        const user = this.create({ username, password: hashedPassword});
        
        // 데이터베이스 레벨에서 만약 같은 이름을 가진 유저가 있다면 에러 던지기 
        try {
            await this.save(user);
        } catch (error) {
            if (error.code === "23505") {
                throw new ConflictException("Existing username");
            } else {
                throw new InternalServerErrorException();
            }
        }
    }
}