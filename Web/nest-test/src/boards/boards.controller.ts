// 들어오는 요청을 처리하고 클라이언트에 응답을 반환함
// @Controller 데코레이터로 클래스를 데코레이션하여 정의함
// Handler : @Get, @Post, @Delete 등과 같은 데코레이터로 장식 된 컨트롤러 클래스 내의 단순한 메서드
import { Body, Controller, Delete, Get, Param, ParseIntPipe, Patch, Post, UseGuards, UsePipes, ValidationPipe } from '@nestjs/common';
import { BoardsService } from './boards.service';
import { BoardStatus } from './board-status.enum';
import { CreateBoardDto } from './dto/create-board.dto';
import { BoardStatusValidationPipe } from './pipes/board-status-validation.pipe';
import { Board } from './board.entity';
import { AuthGuard } from '@nestjs/passport';
import { GetUser } from 'src/auth/get-decorator';
import { User } from 'src/auth/user.entity';

@Controller('boards')
// 인증된 유저만 게시물 보고 쓸 수 있게 하기 
@UseGuards(AuthGuard())
export class BoardsController {
    constructor(private boardsService : BoardsService) {}
    
    // 모든 게시물 조회하기
    @Get("/")
    getAllBoard(
        // 해당 유저의 게시물만 가져오기 (getAllBoards)
        @GetUser() user: User
    ): Promise<Board[]> {
        return this.boardsService.getAllBoards(user);
    }

    // 게시물 생성하기 + 유효성 체크하기 
    @Post()
    @UsePipes(ValidationPipe)
    createBoard(@Body() createBoardDto: CreateBoardDto,
    @GetUser() user:User): Promise<Board> {
        return this.boardsService.createBoard(createBoardDto, user)
    }
    // @Post()
    // @UsePipes(ValidationPipe)
    // createBoard(
    //     @Body() createBoardDto: CreateBoardDto
    // ): Board {
    //     return this.boardsService.createBoard(createBoardDto)
    // }
    
    // ID로 특정 게시물 가져오기
    @Get("/:id")
    getBoardByID(@Param("id") id:number) : Promise<Board> {
        return this.boardsService.getBoardById(id);
    }
    // @Get("/:id")
    // getBoardByID(@Param("id") id: string): Board {
    //     return this.boardsService.getBoardById(id)
    // }

    // ID 로 특정 게시물 삭제하기
    @Delete("/:id")
    deleteBoard(@Param("id",ParseIntPipe) id): Promise<void> {
        return this.boardsService.deleteBoard(id);
    }
    // @Delete("/:id")
    // deleteBoard(@Param("id") id: string): void {
    //     this.boardsService.deleteBoard(id);
    // }

    // 특정 게시물의 상태 업데이트 
    @Patch("/:id/status")
    updateBoardStatus(
        @Param("id", ParseIntPipe) id: number,
        @Body('status', BoardStatusValidationPipe) status: BoardStatus
    ) {
        return this.boardsService.updateBoardStatus(id, status);
    }
}
