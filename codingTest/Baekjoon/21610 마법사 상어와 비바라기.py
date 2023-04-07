# 마법사 상어와 비바라기
# 비바라기를 시전하면 하늘에 비구름을 만들 수 있다
# N×N인 격자에서 연습
# 격자의 각 칸에는 바구니가 하나 있고, 바구니는 칸 전체를 차지
# 바구니에 저장할 수 있는 물의 양에는 제한이 없음
# A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양

# 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)
# 연습 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결
# N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있음

# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다
# 구름에 이동을 M번 명령 (구름은 칸 전체를 차지)
# i번째 이동 명령은 방향 di과 거리 si
#     방향 : 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 1) 모든 구름이 di 방향으로 si칸 이동
# 2) 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
# 3) 구름이 모두 사라짐
# 4) 2) 에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전
#     대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가
#     이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아님
# 5) 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어듦
# 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 함

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합

# 첫째 줄에 N, M
# 둘째 줄부터 N개의 줄에는 N개의 정수
# r번째 행의 c번째 정수는 A[r][c]
# M개의 줄에는 이동의 정보 di 방향으로 si칸 이동

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 방향 : 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름의 위치
queue = deque()
# (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름
# deque([[3, 0], [3, 1], [4, 0], [4, 1]])
queue.append([n - 2, 0])
queue.append([n - 2, 1])
queue.append([n - 1, 0])
queue.append([n - 1, 1])

#  M개의 줄에는 이동의 정보 di 방향으로 si칸 이동
for _ in range(m):
    cloud = [[0] * n for _ in range(n)]
    d, s = map(int, input().split())

    while queue:
        # 큐에 존재하는 구름들의 위치로 방향과 거리만큼 구름을 이동
        x, y = queue.popleft()
        # 방향 대로 이동 (왼, 오른이랑 위, 아래랑 붙어있음)
        nx = (x + dx[d - 1] * s) % n
        ny = (y + dy[d - 1] * s) % n
        # 구름 위치 = 1
        cloud[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            # 구름이 있다면 물의 양 1 추가
            if cloud[i][j] == 1:
                board[i][j] += 1
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                x, y = i, j
                cnt = 0
                # 대각선으로 살펴서 물이 들어있는 바구니의 수를 카운트
                # 해당 숫자만큼 바구니에 물을 채우기
                for k in [1, 3, 5, 7]:
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 대각선에 물이 있다면
                        if board[nx][ny] > 0:
                            cnt += 1
                board[x][y] += cnt
    for i in range(n):
        for j in range(n):
            # 물의 양 2 이상이고, 구름이 없었던 부분만
            if board[i][j] >= 2 and cloud[i][j] == 0:
                board[i][j] -= 2
                # 너희들이 이제 구름이당!
                queue.append([i, j])

# 바구니에 들어있는 물의 양의 합
result = 0
for i in range(n):
    result += sum(board[i])
print(result)
