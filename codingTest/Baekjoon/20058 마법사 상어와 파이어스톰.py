# 마법사 상어와 파이어스톰
# 마법사 상어는 파이어볼과 토네이도를 조합해 파이어스톰을 시전
# 파이어스톰을 크기가 2N × 2N인 격자로 나누어진 얼음판에서 연습
# 위치 (r, c)는 격자의 r행 c열을 의미
# A[r][c]는 (r, c)에 있는 얼음의 양
# A[r][c]가 0인 경우 얼음이 없는 것

# 파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정
# 격자를 2L × 2L 크기의 부분 격자로 나눈다
# 모든 부분 격자를 시계 방향으로 90도 회전
# 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어듦
# (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)

# 마법사 상어는 파이어스톰을 총 Q번 시전
# 1) 남아있는 얼음 A[r][c]의 합
# 2) 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 얼음 칸이 얼음 칸과 인접해 있으면, 두 칸을 연결 (덩어리는 연결된 칸의 집합)

# 첫째 줄에 N과 Q
# 둘째 줄부터 2N개의 줄에는 격자의 각 칸에 있는 얼음의 양
# 마지막 줄에는 마법사 상어가 시전한 단계 L1, L2, ..., LQ

import copy
from collections import deque

n, q = map(int, input().split())
nn = 2**n
# 시계 방향 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(nn)]


# rotate() : 격자판을 l의 따라 나누어서 나눈 부분을 90도 회전
# 처음 board값을 b에 복사한 후 (zip() 사용 회전시킨 값들을 다시 board에 복사
def rotate(l):
    b_n = 2**l
    # 2 ** l 크기의 격자판
    for i in range(nn // b_n):
        for j in range(nn // b_n):
            b = []
            for p in range(b_n):
                col = []
                for k in range(b_n):
                    col.append(board[b_n * i + p][b_n * j + k])
                b.append(col)
            temp = []
            # zip 이 동일 위치 요소 갖고오는데 reverse 해서 거꾸로 받음
            for item in zip(*b):
                temp.append(list(reversed(item)))
            for p in range(b_n):
                for k in range(b_n):
                    board[b_n * i + p][b_n * j + k] = temp[p][k]


def bfs(x, y, visited):
    global max_m
    cnt = 1
    queue = deque()
    queue.append((x, y))
    # 방문함~
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 격자 안이고, 방문 안했다면
            if 0 <= nx < nn and 0 <= ny < nn and not visited[nx][ny]:
                # 얼음이 있다면
                if board[nx][ny] > 0:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    max_m = max(max_m, cnt)


# 마법사 상어가 시전한 단계 L1, L2, ..., LQ
l_lst = list(map(int, input().split()))
for l in l_lst:
    # 나눌 필요없이 전체 90도를 돌림
    if l == n:
        tmp = []
        b = copy.deepcopy(board)
        # 시계방향 돌려돌려
        for item in zip(*b):
            tmp.append(list(reversed(item)))
        board = copy.deepcopy(tmp)
    # 격자크기 만큼 나눠서 돌려돌려
    elif l > 0:
        rotate(l)
    # l == 0 이면 1 x 1 이니까 회전할 필요 없음

    ice = [[0] * nn for _ in range(nn)]

    for i in range(nn):
        for j in range(nn):
            x, y = i, j
            ice_cnt = 0
            # 얼음 없으면 패스
            if board[i][j] == 0:
                continue
            # 근처에 얼음의 갯수가 3개 이상이 아니면 얼음의 양을 -1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < nn and 0 <= ny < nn:
                    if board[nx][ny] > 0:
                        ice_cnt += 1
            if ice_cnt < 3:
                ice[i][j] = (board[i][j] - 1)
            else:
                ice[i][j] = board[i][j]
    board = copy.deepcopy(ice)

s = 0
visited = [[False] * nn for _ in range(nn)]
max_m = 0
for i in range(nn):
    for j in range(nn):
        s += board[i][j]
        if board[i][j] != 0 and not visited[i][j]:
            bfs(i, j, visited)

print(s)
if max_m == 1:
    print(0)
else:
    print(max_m)
