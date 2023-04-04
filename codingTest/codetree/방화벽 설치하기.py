# codetree 참고함
# 방화벽 설치하기
# n * m 크기의 이차원 영역에 방화벽을 설치하여 불로 인한 피해를 최소화
# 불은 상하좌우의 인접한 공간으로 모두 번지는 특성, 방화벽을 뚫을 수는 없음
# 기존에 이미 설치되어 있는 방화벽을 제외하고 추가로 3개의 방화벽을 설치할 수 있을 때 
# 정확히 3개의 방화벽을 추가로 설치하여 불이 퍼지지 않는 영역이 최대일 때의 크기를 출력

# 첫 번째 줄에는 n과 m,
# 두 번째 줄부터 (n+1)번째 줄까지는 각 행에 불 2, 방화벽 1, 빈 칸 0

# 모든 불을 큐에 넣은뒤 BFS -> 가능한 모든 위치에서 한꺼번에 BFS 탐색

from collections import deque

# n * m 크기
n, m = map(int, input().split())

# 불 2, 방화벽 1, 빈 칸 0
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

empty_places = []
selected_indices = []
queue = deque()
max_empty_cnt = 0

# 주어진 위치로 이동할 수 있는지 여부 (크기 안에 있고, 방문 안했고, 방화벽이 아니다)
def can_go(x, y):
    return 0 <= x and x < n and 0 <= y and y < m and not visited[x][y] and grid[x][y] != 1

# visited 배열을 초기화
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

# BFS 탐색을 위해 존재하는 불을 queue에 넣기
def enqueue_fires():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:     # 불이면
                queue.append((i, j))
                visited[i][j] = True

# 선택된 위치에 방화벽을 설치
def place_firewalls():
    for i in range(len(selected_indices)):
        idx = selected_indices[i]
        curr_x, curr_y = empty_places[idx]
        
        grid[curr_x][curr_y] = 1        # 방화벽

# 다음 탐색을 위해 설치했던 방화벽을 제거
def remove_firewalls():
    for i in range(len(selected_indices)):
        idx = selected_indices[i]
        curr_x, curr_y = empty_places[idx]
        
        grid[curr_x][curr_y] = 0        # 빈칸

# 선택된 빈 칸에 방화벽을 설치했을 때 영역의 크기
def get_area():
    global max_empty_cnt 
    
    # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # BFS 탐색을 위한 초기화 (방문한곳, 방화벽 생성, 불위치)
    initialize_visited()
    place_firewalls()
    enqueue_fires()
    
    # BFS 탐색
    while queue:
        curr_x, curr_y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):        # 불 + 4방향 탐색
            new_x, new_y = curr_x + dx, curr_y + dy
        
            if can_go(new_x, new_y):
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                
    # BFS 탐색 과정에서 방문한 적이 없는 빈 칸의 개수
    empty_cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 0:
                empty_cnt += 1
    
    max_empty_cnt = max(empty_cnt, max_empty_cnt)
    
    # 탐색이 끝난 뒤 설치한 방화벽을 제거
    remove_firewalls()

def search_combinations(curr_idx, cnt):
    if cnt == 3:        # 방화벽 세개 끝
        get_area()
        return
    
    if curr_idx == len(empty_places):
        return
    
    selected_indices.append(curr_idx)
    search_combinations(curr_idx + 1, cnt + 1)
    selected_indices.pop()      # 오른쪽 빠짐
    
    search_combinations(curr_idx + 1, cnt)

# 빈 칸인 경우 가능한 조합을 탐색하기 위해 배열에 따로 저장
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            empty_places.append((i, j))
            
search_combinations(0, 0)
print(max_empty_cnt)

##################예제######################
"""
입력:
5 5
2 1 0 0 0
0 1 0 1 1
1 0 1 2 0
0 0 1 0 0
0 1 0 0 0

출력:
12
"""
