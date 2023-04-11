# 얼음 문제
# N X M 크기의 얼음 틀
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
# 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주
# 이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램

# N X M 얼음 틀
n, m = map(int, input().split())
# 얼음 틀 정보
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
	# 범위에 벗어나면 False
	if x < 0 or x >= n or y < 0 or y >= m:
		return False
	# 구멍 뚫림
	if graph[x][y] == 0:
		graph[x][y] = 1
		# 상, 하, 좌, 우로 붙어있는 경우 서로 연결
		dfs(x+1, y)
		dfs(x-1, y)
		dfs(x, y+1)
		dfs(x, y-1)
		return True
	# 방문한 노드일 경우 False
	return False

result = 0
for i in range(n):
	for j in range(m):
		if dfs(i,j) == True:
			result += 1
print(result)