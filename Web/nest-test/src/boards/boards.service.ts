// 다른 컴포넌트에서 이 서비스를 사용할 수 있게 만들어줌
// @Injectable 데코레이터로 감싸져서 모듈에 제공

import { Injectable } from '@nestjs/common';
import { Board } from './board.model';

@Injectable()
export class BoardsService {
    // [] 로 타입 지정함 
    private boards: Board[] = [];

    // 모든 게시물 조회하기
    getAllBoards(): Board[] {
        return this.boards;
    }
}
