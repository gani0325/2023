from collections import deque

# 격자 한 변의 크기 N, 색상의 개수 M
n, m = map(int, input().split())
# 격자의 칸에 들어있는 블록의 정보 (검은색 블록, 무지개 블록, 일반 블록은 M가지 색상)
board = [list(map(int, input().split())) for _ in range(n)]

# 반시계 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, visited, b_num):
    queue = deque()
    queue.append((x, y))
    # 블록 정보
    c = board[x][y]
    # 일반 블록은 M가지 색상, 검은색 블록은 -1, 무지개 블록은 0
    # 방문처리 + 블록 그룹 번호 저장
    visited[x][y] = b_num
    size, r_n = 1, 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == c and visited[nx][ny] == 0:
                    size += 1
                    visited[nx][ny] = b_num
                    queue.append((nx, ny))
                elif board[nx][ny] == 0 and not b_num in visited[nx][ny]:
                    size += 1
                    r_n += 1
                    visited[nx][ny].append(b_num)
                    queue.append((nx, ny))
    # 블록 그룹의 사이즈와, 블록 그룹 안에 있는 무지개 블록의 갯수
    return size, r_n

# 중력
def fall(x, y) :
    stop = False
    for i in range(x + 1, n) :
        nx = i
        if board[nx][y] != -2 :
            stop = True
            break
    if stop :
        board[nx-1][y] = board[x][y]
    else :
        board[nx][y] = board[x][y]
    # 블록을 제거한다. 제거 시 -2값으로 변경한다. 
    board[x][y] = -2

score = 0
while True:
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                visited[i][j] = []

    b_num, block = 1, []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == 0:
                # # 블록 그룹의 사이즈와, 블록 그룹 안에 있는 무지개 블록의 갯수
                size, r_n = bfs(i, j, visited, b_num)
                if size > 1:
                    # 그룹의 크기, 무지개블록의 갯수, 블록 기준 행, 열, 블록 번호
                    block.append([size, r_n, i, j, b_num])
                b_num += 1
    if len(block) == 0:
        break
    # 블록 그룹의 크기 -> 무지개 블록의 갯수 -> 블록 기준의 행 -> 열
    block.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == block[0][4]:
                count += 1
                board[i][j] = -2
            elif board[i][j] == 0 and block[0][4] in visited[i][j]:
                count += 1
                board[i][j] = -2

    score += (count*count)
    for i in range(n-2, -1, -1):
        for j in range(n):
            # 블록을 제거한다. 제거 시 -2값으로 변경한다. 
            if board[i][j] >= 0 and board[i+1][j] == -2:
                fall(i, j)

    board = list(map(list, zip(*board)))[::-1]

    for i in range(n-2, -1, -1):
        for j in range(n):
            # 블록을 제거한다. 제거 시 -2값으로 변경한다. 
            if board[i][j] >= 0 and board[i+1][j] == -2:
                fall(i, j)


print(score)