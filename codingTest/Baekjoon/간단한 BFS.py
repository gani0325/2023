# 미로게임
# 동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혔다
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다
# 동빈이의 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동
# 이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시
# 미로는 반드시 탈출할 수 있는 형태로 제시

# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수
# 칸을 셀때는 시작 칸과 마지막 칸을 모두 포함해서 계산

from collections import deque
# N X M 미로
n, m = map(int, input().split())
# 미로의 정보
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	queue = deque()
	queue.append([x, y])
	while queue:
		# 값 초기화
		x, y = queue.popleft()
		# 4가지 방향
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 범위 벗어난 경우 무시
			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			# 괴물 있는 경우 무시
			if graph[nx][ny] == 0:
				continue
			# 괴물이 없는 부분이다!
			# 현재 위치에서 이동!
			if graph[nx][ny] == 1:
				queue.append([nx,ny])
				graph[nx][ny] = graph[x][y] + 1
bfs(0,0)
print(graph)
print(graph[n-1][m-1])