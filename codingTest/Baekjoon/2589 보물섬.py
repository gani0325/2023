"""
[2589] 보물섬

💛 문제
보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 
보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 
각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 
한 칸 이동하는데 한 시간이 걸린다. 

보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 
육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.

보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

💚 입력
첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다. 
이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 
보물 지도의 가로, 세로의 크기는 각각 50이하이다.

💙 출력
첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.
"""

from collections import deque

# 보물 지도의 세로의 크기와 가로의 크기
N, M = map(int, input().split())

good = []
graph = []

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1] 

for i in range(N):
    temp = list(map(str, input()))
    for j in range(len(temp)):
        # 각 칸은 육지(L)나 바다(W)
        if temp[j] == 'L':
            graph.append((i, j))
    good.append(temp)


def bfs(r, c):
    queue = deque([[r, c, 0]])
    visited[r][c] = True
    
    while queue:
        r, c, distance = queue.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            
            if 0 <= nx < N and 0 < ny < M :
                visited[nx][ny] = True
                queue.append([nx, ny, distance + 1])
    return distance


result = 0
for i in range(len(graph)):
    visited = [[False] * M for _ in range(N)]
    distance = bfs(graph[i][0], graph[i][1])
    if result < distance:
        result = distance

print(result)