// 들어오는 요청을 처리하고 클라이언트에 응답을 반환함
// @Controller 데코레이터로 클래스를 데코레이션하여 정의함
// Handler : @Get, @Post, @Delete 등과 같은 데코레이터로 장식 된 컨트롤러 클래스 내의 단순한 메서드
import { Controller, Get } from '@nestjs/common';
import { BoardsService } from './boards.service';
import { Board } from './board.model';

@Controller('boards')
export class BoardsController {
    constructor(private boardsService : BoardsService) {}
        
    @Get("/")
    getAllBoard(): Board[] {
        return this.boardsService.getAllBoards();
    }
}
