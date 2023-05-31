## 따라하면서 배우는 NestJS

https://www.youtube.com/watch?v=3JminDpCJNE

## 프로젝트 설치

```bash
$ npm i -g @nestjs/cli
$ nest new project-name
```

🎀 .eslintrc.js

: 개발자들이 특정한 규칙을 가지고 코드를 깔끔하게 짤 수 있게 도와주는 라이브러리

: 타입스크립트를 쓰는 가이드 라인 제시, 문법 오류 알려줌

🎀 .prettierrc

: 코드 형식을 맞추는데 사용

ex) 작은 따옴표인지 큰 따옴표인지, indent 값 설정 등

🎀 nest-cli.json

: nest 프로젝트를 위해 특정한 설정을 할 수 있는 json 파일

🎀 tsconfig.json

: 어떻게 타입스크립트를 컴파일 할지 설정

🎀 tsconfig.build.json

: build 할 때 필요한 설정들

: "excludes" 에서는 빌드할 때 필요없는 파일들 명시

🎀 pacage.json

: build 는 운영환경을 위한 빌드

: format 은 프린트 에러가 났을지 수정

: start 은 앱 시작

## Description

[Nest](https://github.com/nestjs/nest) framework TypeScript starter repository.

## Installation

```bash
$ npm install
```

## Running the app

```bash
# development
$ npm run start

# watch mode
$ npm run start:dev

# production mode
$ npm run start:prod
```

## Test

```bash
# unit tests
$ npm run test

# e2e tests
$ npm run test:e2e

# test coverage
$ npm run test:cov
```

## Support

Nest is an MIT-licensed open source project. It can grow thanks to the sponsors and support by the amazing backers. If you'd like to join them, please [read more here](https://docs.nestjs.com/support).

## Stay in touch

- Author - [Kamil Myśliwiec](https://kamilmysliwiec.com)
- Website - [https://nestjs.com](https://nestjs.com/)
- Twitter - [@nestframework](https://twitter.com/nestframework)

## License

Nest is [MIT licensed](LICENSE).
