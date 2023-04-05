# 연구소 3
# 바이러스는 활성 상태와 비활성 상태
# 가장 처음에 모든 바이러스는 비활성 상태
# 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸림
# 연구소의 바이러스 M개를 활성 상태로 변경하려고 함
# 연구소는 크기가 N×N인 정사각형 (1×1 크기의 정사각형으로 나뉨)
# 연구소는 0은 빈 칸, 1은 벽, 2는 바이러스의 위치
# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변함

# 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간 구하
# 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.

# 첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)
# 둘째 줄부터 N개의 줄에 연구소의 상태
# 0은 빈 칸, 1은 벽, 2는 바이러스 (M보다 크거나 같고, 10보다 작거나 같은 자연수)

from collections import deque
import copy

# 연구소의 크기 N, 놓을 수 있는 바이러스의 개수
n, m = map(int, input().split())
graph = []
virus = []
# 최소 시간
min_time = int(1e9)
# 북 동 남 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if data[j] == 2:
            # 비활성화 바이러스
            graph[i][j] == -1
            # 바이러스 위치
            virus.append((i, j))


def check(g):
    for i in range(n):
        for j in range(n):
            # 빈 칸인가
            if g[i][j] == 0:
                return False
    return True


def combi(lst, num):
    result = []
    if num > len(lst):
        return result
    if num == 1:
        for l in lst:
            result.append([l])
    elif num > 1:
        for i in range(len(lst) - num + 1):
            for t in combi(lst[i + 1:], num - 1):
                result.append(t + [lst[i]])
    return result


def bfs(g, combination):
    global min_time
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    if check(g):
        min_time = min(min_time, 0)
        return

    for c in combination:
        a, b = c
        visited[a][b] = True
        # 활성 바이러스
        g[a][b] = -2
        # 위치와 걸린 시간
        queue.append((a, b, 0))
    end_time = 0

    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 벽이면
                if g[nx][ny] == 1:
                    continue
                else:  # 빈칸이면
                    if g[nx][ny] == 0:
                        end_time = max(end_time, time + 1)
                    # 활성 바이러스
                    g[nx][ny] = -2
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))
    if check(g):
        min_time = min(min_time, end_time)


g = copy.deepcopy(graph)
for com in combi(virus, m):
    g = copy.deepcopy(g)
    bfs(g, com)
    g = graph

if min_time == int(1e9):
    print(-1)
else:
    print(min_time)
