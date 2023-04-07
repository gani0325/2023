# 마법사 상어와 토네이도
# 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습
# 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작
# 토네이도는 한 번에 한 칸 이동
# 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날fla
# 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해짐

# 토네이도는 (1, 1)까지 이동한 뒤 소멸
# 모래가 격자의 밖으로 이동할 수도 있다
# 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양

# 첫째 줄에 격자의 크기 N
# 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래
#    r번째 줄에서 c번째 주어지는 정수는 A[r][c]

n = int(input())
# 왼쪽, 아래쪽, 오른쪽, 위쪽
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# 격자 n X n, A[r][c]는 (r, c)에 있는 모래의 양
board = [list(map(int, input().split())) for _ in range(n)]
# 토네이도가 이동했을 때 위치와 방향
go_dict = {}

# 토네이도 처음 중심 위치
x, y = n // 2, n // 2
cnt = 0
d = 0

# 토네이도에 방향을 유지한채 이동하는 거리
go = []
for i in range(1, n):
    go.append(i)
    go.append(i)
go.append(n)

g_idx = 0
# 해당 위치 행,열 값과 다음 이동 방향
go_dict[1] = [x, y, 0]
sand = 0

# 토네이도가 한 칸 이동할 때마다 모래는 일정한 비율로 흩날리게 됨 (-1 : 알파)
# 0 0  2 0 0
# 0 10 7 1 0
# 6 -1 S 0 0
# 0 10 7 1 0
# 0 0  2 0 0
left = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, -1, 0, 0, 0], [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]]
right = [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, -1, 5], [0, 1, 7, 10, 0],
         [0, 0, 2, 0, 0]]
up = [[0, 0, 5, 0, 0], [0, 10, -1, 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0]]
down = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, -1, 10, 0],
        [0, 0, 5, 0, 0]]


# 모래를 흩날리는 양의 알파 부분은 나머지 부분을 비율에 맞춰서 흩날린 후, 남은 양을 옮김
# 흩날릴 부분이 격자 밖이면 sand에 값을 더해주고, 격자 안이면 해당 인덱스에 맞춰 격자판에 더함
# 위치 (x, y), 모래 양, 모래 비율 4가지 중 하나
def moving(x, y, a, plus):
    global sand
    a_x, a_y = -1, -1
    remain = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            if plus[i + 2][j + 2] == 0 or plus[i + 2][j + 2] == -1:
                if plus[i + 2][j + 2] == -1:
                    a_x, a_y = i + 2, j + 2
                continue
            temp = int(a * (plus[i + 2][j + 2] / 100))
            remain += temp
            # 흩날린 모래가 격자밖으로 넘어가면
            if x + i < 0 or x + i >= n or y + j < 0 or y + j >= n:
                sand += temp
            else:
                board[x + i][y + j] += temp
    # α의 모래 양 : 비율이 적혀있는 칸으로 이동하지 않은 남은 모래 양
    if 0 <= x + a_x - 2 < n and 0 <= y + a_y - 2 < n:
        board[x + a_x - 2][y + a_y - 2] += (a - remain)
    else:
        sand += (a - remain)


for i in range(1, n * n):
    nx = x + dx[d]
    ny = y + dy[d]
    cnt += 1
    x, y = nx, ny
    # go = 이동 거리 1, 1, 2, 2, 3, 3, 4, 4, 5, 5 ... n-1, n-1, n
    # go[g_idx]만큼 이동했으면 방향을 바꾸고 g_idx 값을 1증가
    # go[g_idx]만큼 이동하지 않았으면 계속 이동한 nx,ny값과 방향을 b_dict에 넣어줌
    if cnt >= go[g_idx]:
        # 방향 0 1 2 3 (왼쪽, 아래, 오른쪽, 위쪽)
        d = (d + 1) % 4
        go_dict[i + 1] = [nx, ny, d]
        g_idx += 1
        cnt = 0
    else:
        go_dict[i + 1] = [nx, ny, d]

for i in range(1, n * n):
    x, y, d = go_dict[i]
    nx, ny, nd = go_dict[i + 1]

    if d == 0:
        moving(nx, ny, board[nx][ny], left)
    elif d == 1:
        moving(nx, ny, board[nx][ny], down)
    elif d == 2:
        moving(nx, ny, board[nx][ny], right)
    else:
        moving(nx, ny, board[nx][ny], up)
    board[nx][ny] = 0

print(sand)