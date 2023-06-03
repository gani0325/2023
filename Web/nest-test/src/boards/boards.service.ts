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

@Injectable()
export class BoardsService {
    constructor(
        @InjectRepository(BoardRepository)
        private boardRepository: BoardRepository,
    ){}

    // // [] 로 타입 지정함 
    // private boards: Board[] = [];

    // // 모든 게시물 조회하기
    // getAllBoards(): Board[] {
    //     return this.boards;
    // }

    // 게시물 생성하기
    async createBoard(createBoardDto: CreateBoardDto): Promise<Board> {
        const {title, description} = createBoardDto;

        const board = this.boardRepository.create({
            title,
            description,
            status: BoardStatus.PUBLIC
        })

        await this.boardRepository.save(board);
        return board;
        
    }
    // createBoard(createBoardDto: CreateBoardDto) {
    //     const {title, description} = createBoardDto;
    
    //     const board: Board = {
    //         id: uuid(),    // 데이터베이스에서 알아서 해주지만, 여기서는 uuid 모듈로 임의로 넣어줌
    //         title,
    //         description,
    //         status: BoardStatus.PUBLIC
    //     }
    //     this.boards.push(board);
    //     return board;
    // }

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

    // // ID로 특정 게시물 삭제하기
    // deleteBoard(id: string): void {
    //     // 있는 ID 의 게시물인지 확인하기
    //     const found = this.getBoardById(id);
    //     this.boards = this.boards.filter((board) => board.id !== found.id);
    // }

    // // 특정 게시물의 상태 업데이트 
    // updateBoardUpdate(id: string, status: BoardStatus): Board {
    //     // 특정 게시물 찾기
    //     const board = this.getBoardById(id);
    //     board.status = status;
    //     return board;
    // }
}
