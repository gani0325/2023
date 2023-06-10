import { Board } from "src/boards/board.entity";
import { BaseEntity, Column, Entity, OneToMany, PrimaryColumn, PrimaryGeneratedColumn, Unique } from "typeorm";

@Entity()
// 유저 이름에 유니크한 값 주기
@Unique(["username"])
export class User extends BaseEntity {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    username: string;

    @Column()
    password: string;
    
    // 유저와 게시물 데이터의 관계 형성
    @OneToMany(type => Board, board => board.user, {eager : true})
    boards: Board()
}