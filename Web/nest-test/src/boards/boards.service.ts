// 다른 컴포넌트에서 이 서비스를 사용할 수 있게 만들어줌
// @Injectable 데코레이터로 감싸져서 모듈에 제공

import { Injectable, NotFoundException } from '@nestjs/common';
import { BoardStatus } from './board-status.enum';
import { CreateBoardDto } from "./dto/create-board.dto";
import { v1 as uuid } from "uuid";
import { create } from 'domain';
import { statSync } from 'fs';
import { BoardRepository } from './board.repository';
import { InjectRepository } from '@nestjs/typeorm';
import { Board } from './board.entity';
import { User } from 'src/auth/user.entity';

@Injectable()
export class BoardsService {
    constructor(
        @InjectRepository(BoardRepository)
        private boardRepository: BoardRepository,
    ){}

    // 모든 게시물 조회하기
    async getAllBoards(
        user: User
    ): Promise <Board[]> {
        // 해당 유저의 게시물만 가져오기 (getAllBoards)
        const query = this.boardRepository.createQueryBuilder("board");
        query.where("board.userId = :userId", { userId: user.id});
        const boards = await query.getMany();
        
        return boards;
    }

    // 게시물 생성하기
    async createBoard(createBoardDto: CreateBoardDto, user: User): Promise<Board> {
        return this.boardRepository.createBoard(createBoardDto, user);       
    }

    // ID로 특정 게시물 가져오기
    async getBoardById(id: number): Promise <Board> {
        const found = await this.boardRepository.findOne(id);

        // 특정 게시물을 찾을 때 없는 경우 결과값 처리하기 
        // 예외 인스턴스 생성하여 에러 표출
        if (!found) {
            throw new NotFoundException(`Can't find Board with id ${id}`);
        }
        return found;
    }
    // getBoardById(id: string): Board {
    //     const found = this.boards.find((board) => board.id === id);
        
    //     // 특정 게시물을 찾을 때 없는 경우 결과값 처리하기 
    //     // 예외 인스턴스 생성하여 에러 표출
    //     if (!found) {
    //         throw new NotFoundException(`Can't find Board with id ${id}`);;
    //     }

    //     return found;
    // }

    // ID로 특정 게시물 삭제하기
    async deleteBoard(id: number): Promise<void> {
        const result = await this.boardRepository.delete(id);

        // ID가 존재하는 게시물이니?
        if (result.affected === 0) {
            throw new NotFoundException(`Can't find Board with id ${id}`);
        }
    }

    // deleteBoard(id: string): void {
    //     // 있는 ID 의 게시물인지 확인하기
    //     const found = this.getBoardById(id);
    //     this.boards = this.boards.filter((board) => board.id !== found.id);
    // }

    // 특정 게시물의 상태 업데이트 
    async updateBoardStatus(id: number, status: BoardStatus): Promise<Board> {
        const board = await this.getBoardById(id);
        board.status = status;
        await this.boardRepository.save(board);
        
        return board;
    }
    // updateBoardUpdate(id: string, status: BoardStatus): Board {
    //     // 특정 게시물 찾기
    //     const board = this.getBoardById(id);
    //     board.status = status;
    //     return board;
    // }
}
