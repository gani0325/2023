"""
[2573] 빙산

💛 문제
지구 온난화로 인하여 북극의 빙산이 녹고 있다. 
빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자. 
빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 
빙산 이외의 바다에 해당되는 칸에는 0이 저장된다. 
그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.
 	 	 	 	 	 	 
 	2	4	5	3	 	 
 	3	 	2	5	2	 
 	7	6	2	4	 	 
 	 	 	 	 	 	 
<그림 1. 행의 개수가 5이고 열의 개수가 7인 2차원 배열에 저장된 빙산의 높이 정보>

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 
배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 
단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 
바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 
따라서 그림 1의 빙산은 일년후에 그림 2와 같이 변형된다.
 	 	 	 	 	 	 
 	 	2	4	1	 	 
 	1	 	1	5	 	 
 	5	4	1	2	 	 
 	 	 	 	 	 	 
<그림 2>

그림 3은 그림 1의 빙산이 2년 후에 변한 모습을 보여준다. 
 	 	 	 	 	 	 
 	 	 	3	 	 	 
 	 	 	 	4	 	 
 	3	2	 	 	 	 
 	 	 	 	 	 	 
<그림 3>

2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다. 
따라서 그림 2의 빙산은 한 덩어리이지만, 그림 3의 빙산은 세 덩어리로 분리되어 있다

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 
그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

💚 입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다.
N과 M은 3 이상 300 이하이다. 
그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 
각 칸에 들어가는 값은 0 이상 10 이하이다. 
배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 
배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

💙 출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 
만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.
"""

# 1) BFS
from collections import deque

def bfs(x, y) :
    # 빙산 위치
    q = deque()
    q.append((x, y))
    # 주변에 바다가 있는 빙산을 (x, y, 바다 갯수)
    visited[x][y] = 1
    seaList = []

    while q :
        x, y = q.popleft()
        sea = 0

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M :
                if not graph[nx][ny] :
                    # 빙산 주변의 바다 갯수
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny] :
                    q.append((nx, ny))
                    visited[nx][ny] = 1
            
        if sea > 0 :
            seaList.append((x, y, sea))
    # 빙산 녹이기
    for x, y, sea in seaList :
        graph[x][y] = max(0, graph[x][y] - sea)
    
    # 하나의 그룹을 탐색
    return 1


N, M = map(int, input().split())
graph = []

for i in range(N) :
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0
ice = []

for i in range(N) :
    for j in range(M) :
        if graph[i][j] :
            # 빙산의 위치를 (i, j)
            ice.append((i, j))

while ice :
    visited = [[0] * (M) for _ in range(N)]
    delList = []

    # bfs() 에서 받아온 빙산 그룹의 개수
    result = 0

    for i, j in ice :
        # 빙산 개수 더하기
        if graph[i][j] and not visited[i][j] :
            result += bfs(i, j)
        # 빙산이 없다면
        if graph[i][j] == 0 :
            delList.append((i, j))

    # 빙산 그룹이 2개 이상이면
    if result > 1 :
        print(year)
        break
    
    # 다 녹은 빙산 제거
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if result < 2 :
    print(0)

# input
# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

# output
# 2