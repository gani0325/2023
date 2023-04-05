# 마법사 상어와 파이어볼
# 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사
# 가장 처음에 파이어볼은 각자 위치에서 이동을 대기
# i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si
# 격자의 행과 열은 1번부터 N번까지 번호
# 파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향 (↑↗→↘↓↙←↖)

# 마법사 상어가 모든 파이어볼에게 이동을 명령
# 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동
#     이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있음
# 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서의 경우
#     a. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐짐
#     b. 파이어볼은 4개의 파이어볼로 나누어짐
#     c. 나누어진 파이어볼의 질량, 속력, 방향
#         - 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
#         - 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
#         - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이고, 그렇지 않으면 1, 3, 5, 7
#     d. 질량이 0인 파이어볼은 소멸되어 없어짐

# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합

# 첫째 줄에 N, M, K
# 둘째 줄부터 M개의 줄에 파이어볼의 정보 (ri, ci, mi, si, di)
# 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않음

# N×N인 격자에 파이어볼 M개, 이동 명령 수 k
n, m, k = map(int, input().split())
# 8개의 칸의 방향 (↑↗→↘↓↙←↖)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    # 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si
    r, c, mm, s, d = map(int, input().split())
    # 현재 파이어볼에 행과 열에 해당하는 정보(질량, 속력, 방향) 저장
    board[r - 1][c - 1].append([mm, s, d])


def move():
    b = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 파이어볼이 없다
            if len(board[i][j]) == 0:
                continue
            for p in board[i][j]:
                x, y = i, j
                mm, s, d = p
                # 이동 후 칸 수 % N로 처리
                nx = (x + dx[d] * s) % n
                ny = (y + dy[d] * s) % n
                b[nx][ny].append([mm, s, d])

    for i in range(n):
        for j in range(n):
            # 파이어볼이 한 개 이하 존재
            if len(b[i][j]) <= 1:
                continue
            # 질량은 (합쳐진 파이어볼 질량의 합)/5
            # 속력은 (합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)
            # 합쳐지는 파이어볼의 방향이 모두 홀수 or 짝수
            #    방향은 0, 2, 4, 6 그렇지 않으면 1, 3, 5, 7
            mm_sum, s_sum, oodd, eeven = 0, 0, True, True
            num = len(b[i][j])
            for p in b[i][j]:
                mm, s, d = p
                mm_sum += mm
                s_sum += s
                # 홀수
                if (d % 2 == 1):
                    eeven = False
                else:
                    oodd = False

            # 초기화 해주고 다시 새로운 정보 넣기
            b[i][j] = []
            # 소멸~
            if mm_sum < 5:
                continue
            else:
                # 모두 홀수 이거나 짝수
                if eeven or oodd:
                    for q in [0, 2, 4, 6]:
                        b[i][j].append([mm_sum // 5, s_sum // num, q])
                else:
                    for q in [1, 3, 5, 7]:
                        b[i][j].append([mm_sum // 5, s_sum // num, q])

    for i in range(n):
        for j in range(n):
            board[i][j] = b[i][j]


for _ in range(k):
    move()

answer = 0
for i in range(n):
    for j in range(n):
        # 현재 남아있는 파이어볼의 질량합을 구해 출력
        for b in board[i][j]:
            answer += b[0]
print(answer)
