# 아기상어
# N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리
# 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다
# 한 칸에는 물고기가 최대 1마리 존재

# 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수
# 가장 처음 아기 상어 크기는 2이고, 1초에 상하좌우로 한 칸씩 이동

# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
#     나머지 칸은 모두 지나갈 수 있다
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다
# 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다

# 아기 상어가 어디로 이동할지 결정하는 방법
# 1) 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청
# 2) 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다
# 3) 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다
#     거리는 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값
#     거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
#         그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다
# 4) 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다
#     아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다
#     물고기를 먹으면, 그 칸은 빈 칸
# 5) 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가

# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램

# 첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)
# 둘째 줄부터 N개의 줄에 공간의 상태
# 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9
#     0: 빈 칸
#     1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
#     9: 아기 상어의 위치
#     아기 상어는 공간에 한 마리 있다

from collections import deque

# 공간의 크기 N(2 ≤ N ≤ 20)
n = int(input())
# 아기 상어 처음 크기
s_level = 2
eat = 0
graph = []
# 아기 상어 처음 위치
s_x, s_y = 0, 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    # 0: 빈 칸
    # 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
    # 9: 아기 상어의 위치
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if data[j] == 9:
            s_x, s_y = i, j

# 아기 상어 위치를 0으로 표기
graph[s_x][s_y] = 0

def bfs(s_x, s_y, s_level):
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    # 상어 위치와 물고기 먹은 개수
    queue.append((s_x, s_y, 0))
    visited[s_x][s_y] = True

    # 현재 아기상어가 먹을 수 있는 물고기 위치, 물고기까지의 이동 거리
    fish = []
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                # 빈칸이 아니고(물고기) 아기 상어보다 level 작으면! => 먹는다
                if graph[nx][ny] != 0 and graph[nx][ny] < s_level:
                    fish.append((cnt + 1, nx, ny))
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True
                # 빈칸이거나 아기 상어 level 과 같으면! => 지나갈 순 있음
                elif graph[nx][ny] == 0 or graph[nx][ny] == s_level:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))

    # 먹을 수 있는 물고기가 존재(fish 리스트의 길이가 1이상) 이라면,
    # sort를 통해 (최단 거리 물고기 - 행 가장 작은 위치 - 열 가장 작은 위치
    # 현재 위치에서 가장 먹을 수 있는 최단 거리의 물고기 정보를 return
    fish.sort()
    if fish:
        return [fish[0][1], fish[0][2], fish[0][0]]
    else:
        return []


answer = 0
while True:
    fish_eat = bfs(s_x, s_y, s_level)
    if fish_eat:
        x, y, move = fish_eat
        # 물고기 먹었으니 0
        graph[x][y] = 0
        eat += 1
        # 아기 상어의 이동은 1초
        answer += move
        if eat == s_level:
            # 먹은 개수랑 아기상어 레벨이 같다면 한단계 상승! 먹은 개수 초기화
            s_level += 1
            eat = 0
        # 아기 상어 위치 -> 먹은 물고기 위치로 변경
        s_x, s_y = x, y
    else:
        break
# 물고기를 잡아먹을 수 있는 시간
print(answer)