## 🖥️ nest

- service <BR>
  주로 데이터베이스와 관련된 로직을 처리
- controller <BR>
  들어오는 요청을 처리하고, client에 요청에 대한 응답을 반환
- provider <bR>
  의존성으로 주입될 수 있는 클래스 <bR>
  services, repositories, factories, helpers 등과 같은 nest의 class들을 provider
- modules <BR>
  어플리케이션의 구조를 정리해주는 metadata를 제공 <Br>

```
import { Module } from '@nestjs/common';

@Module({
  controllers: [],
  providers: [],
  imports: [],
  exports: [],
})

export class CatsModule {}

// controllers: 생성되어야 하는 controllers
// providers: 모듈 내에서 inject되어 사용될 수 있는 클래스
// imports: 모듈 내에서 사용할 수 있도록 import되어진 providers
// exports: 다른 모듈에서 사용할 수 있도록 export하고자 하는 providers
```
