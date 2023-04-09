from collections import deque

# 세로, 가로 크기
n, m = map(int, input().split())
graph = []
dx = [-1 ,0, 1, 0]
dy = [0, 1, 0, -1]
rx, ry, bx, by = 0, 0, 0, 0
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n) :
    data = list(input())
    graph.append(data)
    for d in range(len(data)) :
        if data[d] == "R" :
            rx, ry = i, d
        elif data[d] == "B" :
            bx, by = i, d

def move(x, y, dx, dy) :
    cnt = 0
    # '#'은 공이 이동할 수 없는 장애물 또는 벽, 'O'는 구멍의 위치
    while graph[x+dx][y+dy] != "#" and graph[x][y] != "O" :
        # 움직이는 것을 종료한 후 움직인 후의 위치와 움직인 횟수
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt
        
def bfs(rx, ry, bx, by) :
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    while queue : 
        r_x, r_y, b_x, b_y, depth = queue.popleft()
        if depth > 10 :
            break
        for i in range(4) :
            r_nx, r_ny, r_cnt = move(r_x, r_y, dx[i], dy[i])
            b_nx, b_ny, b_cnt = move(b_x, b_y, dx[i], dy[i])
            # 기울린 후 파란 구슬의 위치가 구멍이 아니면서 빨간 구슬의 위치가 구멍이라면 기울린 횟수(depth)
            if graph[b_nx][b_ny] != "O" :
                if graph[r_nx][r_ny] == "O" :
                    return depth
                # 빨강, 파랑 구슬 같이 있을 수 없음
                if r_nx == b_nx and r_ny == b_ny :
                    if r_cnt > b_cnt :
                        r_nx -= dx[i]
                        r_ny -= dy[i]
                    else : 
                        b_nx -= dx[i]
                        b_ny -= dy[i]
                if not visited[r_nx][r_ny][b_nx][b_ny] :
                    visited[r_nx][r_ny][b_nx][b_ny] = True
                    queue.append((r_nx, r_ny, b_nx, b_ny, depth + 1))
    return -1

print(bfs(rx, ry, bx, by))