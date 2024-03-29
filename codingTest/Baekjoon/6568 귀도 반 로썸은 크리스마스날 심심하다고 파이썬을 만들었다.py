"""
[6568] 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다

💛 문제
그래서 여러분도 크리스마스날 심심해서 컴퓨터를 하나 만들었다. 
이 컴퓨터는 아주 적은 수의 명령어를 사용하는 하나의 프로세서, 
32바이트 메모리, 8비트짜리 가산기, 5비트짜리 프로그램 카운터(pc)로 이루어져 있다. 

폰 노이만 구조를 표방하여 이 컴퓨터는 메모리와 프로그램 구문을 공유한다.
프로그램 카운터는 다음에 실행되어야 하는 명령어의 주소를 갖고 있다. 
각 명령어의 길이는 1바이트이며, 상위 3비트는 명령어의 종류를, 하위 5비트는 피연산자를 표현한다. 
피연산자는 언제나 메모리 값(XXXXX)이다. 피연산자가 필요하지 않은 명령어도 있는데, 이때는 하위 5비트는 무의미하다(-----). 
사용되는 명령어들의 의미는 다음과 같다.

000xxxxx   STA x   메모리 주소 x에 가산기의 값을 저장한다.
001xxxxx   LDA x   메모리 주소 x의 값을 가산기로 불러온다.
010xxxxx   BEQ x   가산기의 값이 0이면 PC 값을 x로 바꾼다.
011-----   NOP     아무 연산도 하지 않는다.
100-----   DEC     가산기 값을 1 감소시킨다.
101-----   INC     가산기 값을 1 증가시킨다.
110xxxxx   JMP x   PC 값을 x로 바꾼다.
111-----   HLT     프로그램을 종료한다.

초기엔 PC와 가산기 값은 모두 0이다. 명령어를 불러와 해독한 뒤, 그 명령어를 실행하기 전에 PC 값은 1 증가한다. 
프로그램은 언제나 종료된다고 가정해도 좋다.

💚 입력
입력은 여러 개의 테스트 케이스로 주어진다. 각 테스트 케이스는 32개의 줄에 걸쳐 각 메모리 값, 즉 코드가 순서대로 8비트 2진수의 형태로 주어진다. 
왼쪽에 있는 비트일수록 상위 비트이다. 입력은 EOF와 함께 종료된다.

💙 출력
각 테스트 케이스마다 한 줄에 걸쳐 프로그램이 종료되었을 때의 가산기 값을 역시 8비트 2진수 형태로 출력한다.
이때도 왼쪽에 출력될수록 상위 비트이다.
"""

table = [int(input().splite()) for _ in range(32)]

while True:

    cmd, x = table[pc], 32
    pc = (pc + 1) % 32

    if cmd == 0: 
        table[x] = a
    elif cmd == 1: 
        a = table[x]
    elif cmd == 2: 
        if not a:
