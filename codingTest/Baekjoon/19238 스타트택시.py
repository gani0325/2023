# 스타트 택시
# 스타트 택시는 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝남

# 택시 기사는 오늘 M명의 승객을 태우는 것이 목표
# 활동 영역은 N×N 크기의 격자, 각 칸은 비어 있거나 벽이 놓여 있음
# 택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동
#     특정 위치로 이동할 때 항상 최단경로로만 이동

# M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동
# 여러 승객이 같이 탑승하는 경우는 없음
# 택시 기사는 한 승객을 태워 목적지로 이동시키는 일을 M번 반복
# 각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있음

# 택시기사가 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고름
#    승객이 여러 명이면 그중 행 번호가 가장 작은 승객
#        그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객
# 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0

# 1) 연료는 한 칸 이동할 때마다 1만큼 소모
# 2) 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
# 3) 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝남
#     승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않음

# 택시와 세 명의 승객의 출발지와 목적지가 표시
# 모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력
#     이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력
#     모든 손님을 이동시킬 수 없는 경우에도 -1을 출력

# 첫 줄에 N, M, 그리고 초기 연료의 양
#     (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전
# 다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도
#    0은 빈칸, 1은 벽
# 다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호
#    행과 열 번호는 1 이상 N 이하의 자연수, 운전을 시작하는 칸은 빈칸
# 그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 목적지의 행과 열 번호
#    모든 출발지와 목적지는 빈칸, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다름

import copy
from collections import deque

# N X N 격자판, M명의 승객, 초기 연료의 양 K
n, m, k = map(int, input().split())
graph = []

for i in range(n):
    # N개의 줄에 걸쳐 백준이 활동할 영역의 지도 (0은 빈칸, 1은 벽)
    data = list(map(int, input().split()))
    array = []
    for d in data:
        # 벽이 있는 부분을 -1, 아무것도 없는 부분은 -2
        if d == 1:
            array.append(-1)
        else:
            array.append(-2)
    graph.append(array)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# 백준이 운전을 시작하는 칸의 행 번호와 열 번호
t_x, t_y = map(int, input().split())
# 1부터 시작하기에 쉽게 연산 하기 우해서 -1 빼주자!
t_x -= 1
t_y -= 1

# M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 목적지의 행과 열 번호
customer = []
for _ in range(m):
    # 택시 고객의 현재 위치와 목적지의 위치를 저장
    a, b, c, d = map(int, input().split())
    customer.append([a, b, c, d])


# 손님과의 거리 계산
def customer_dist(graph, t_x, t_y):
    g = copy.deepcopy(graph)
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    # 택시
    queue.append((t_x, t_y))
    # 택시 있는 곳은 빈칸임
    g[t_x][t_y] = 0
    visited[t_x][t_y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or n <= nx or 0 > ny or n <= ny:
                continue
            if g[nx][ny] == -1 or visited[nx][ny] == True:
                continue
            g[nx][ny] = g[x][y] + 1
            visited[nx][ny] = True
            queue.append((nx, ny))
    return g


while True:
    # 연료 부족
    if k < 0:
        break
    # 손님 끝!
    if len(customer) == 0:
        break
    move = []
    gg = customer_dist(graph, t_x, t_y)

    # 택시 - 손님
    for c in customer:
        # 택시 고객의 현재 위치와 목적지의 위치를 저장
        a, b, c, d = c
        dis = gg[a - 1][b - 1]
        if dis < 0:
            continue
        move.append([dis, a - 1, b - 1, c - 1, d - 1])
    if len(move) == 0:
        # 연료는 한 칸 이동할 때마다 1만큼 소모
        k = -1
        break
    else:
        # 거리 내림차순 - 행 내림차순 - 열 내림차순
        move.sort(key=lambda x: (x[0], x[1], x[2]))
        # 손님 - 도착지
        if move[0][0] > k:
            k = -1
            break
        else:
            k -= move[0][0]
            t_x, t_y, a, b = move[0][1:]
            end = customer_dist(graph, t_x, t_y)
            d = end[a][b]

            if d < 0:
                # 연료는 한 칸 이동할 때마다 1만큼 소모
                k = -1
                break
            # 거리만큼 연료 빼기
            k -= d
            if k >= 0:
                k += (d * 2)
                customer.remove([t_x + 1, t_y + 1, a + 1, b + 1])
                # 손님의 목적지가 이제 택시 위치
                t_x, t_y = a, b
            else:
                # 연료는 한 칸 이동할 때마다 1만큼 소모
                k = -1
                break

print(k)