// @Module () 데코레이터로 주석이 달린 클래스
// Nest 가 애플리케이션 구조를 구성하는데 사용하는 메타 데이터를 제공
// 모듈은 밀접하게 관련된 기능 집합으로 구성 요소를 구성함 (기능별로 만들기)

import { Module } from '@nestjs/common';
import { BoardsController } from './boards.controller';
import { BoardsService } from './boards.service';

@Module({
  controllers: [BoardsController],
  providers: [BoardsService]
})
export class BoardsModule {}
