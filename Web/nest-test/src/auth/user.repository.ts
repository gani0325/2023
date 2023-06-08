import { CustomRepositoryCannotInheritRepositoryError, EntityRepository, Repository } from "typeorm";
import { User } from "./user.entity";
import { AuthCredentialsDto } from "./dto/auth-credential.dto";
import { ConflictException, InternalServerErrorException } from "@nestjs/common";

@EntityRepository(User)
export class UserRepository extends Repository<User> {
    async createUser(authCredentialsDto: AuthCredentialsDto): Promise<void> {
        const { username, password } = authCredentialsDto;
        const user = this.create({ username, password });
        
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