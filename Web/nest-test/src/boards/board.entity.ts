import { BaseEntity, Column, Entity, ManyToMany, PrimaryGeneratedColumn } from "typeorm";
import { BoardStatus } from "./board-status.enum";
import { User } from "src/auth/user.entity";

// Board 클래스가 엔티티임을 나타내는데 사용
@Entity()
export class Board extends BaseEntity {
    @PrimaryGeneratedColumn()
    id:number;

    @Column()
    title: string;

    @Column()
    description: string;

    @Column()
    status: BoardStatus;
    
    // 유저와 게시물 데이터의 관계 형성
    @ManyToMany(type => User, user => user.boards, { eager: false })
    user: User;
}