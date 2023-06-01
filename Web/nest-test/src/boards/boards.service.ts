// 다른 컴포넌트에서 이 서비스를 사용할 수 있게 만들어줌
// @Injectable 데코레이터로 감싸져서 모듈에 제공

import { Injectable } from '@nestjs/common';
import { Board, BoardStatus } from './board.model';
import { CreateBoardDto } from "./dto/create-board.dto";
import { v1 as uuid } from "uuid";

@Injectable()
export class BoardsService {
    // [] 로 타입 지정함 
    private boards: Board[] = [];

    // 모든 게시물 조회하기
    getAllBoards(): Board[] {
        return this.boards;
    }

    // 게시물 생성하기
    createBoard(createBoardDto: CreateBoardDto) {
        const {title, description} = createBoardDto;
    
        const board: Board = {
            id: uuid(),    // 데이터베이스에서 알아서 해주지만, 여기서는 uuid 모듈로 임의로 넣어줌
            title,
            description,
            status: BoardStatus.PUBLIC
        }
        this.boards.push(board);
        return board;
    }
}
