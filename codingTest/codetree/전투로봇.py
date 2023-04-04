# codetree 참고함
# 전투 로봇
# n * n 격자판에 m개의 몬스터와 하나의 전투로봇 (한 칸에는 몬스터가 하나 이상 존재할 수 없음)
# 전투로봇과 몬스터 모두 자연수인 레벨
# 초기의 전투로봇의 레벨은 2이고, 전투로봇은 1초에 상하좌우로 인접한 한 칸씩 이동
# 전투로봇은 자신의 레벨보다 큰 몬스터가 있는 칸은 지나칠 수 없고, 나머지 칸은 모두 지날 수 있음
# 전투로봇은 자신의 레벨보다 낮은 몬스터만 없앨 수 있음 (레벨이 같은 몬스터는 없애지는 못하지만, 해당 칸을 지나칠 수 있음)

# 전투로봇이 어디로 이동할지 정하는 규칙
# 1. 없앨 수 있는 몬스터가 있다면 해당 몬스터를 없애러 감
# 2. 없앨 수 있는 몬스터가 하나 이상이라면, 거리가 가장 가까운 몬스터를 없애러 감
# 거리는 해당 칸으로 이동할 때 지나야하는 칸의 개수의 최솟값
# 가장 가까운 거리의 없앨 몬스터가 하나 이상이라면 가장 위 몬스터, 가장 위에 존재하는 몬스터가 여럿이라면 가장 왼쪽 몬스터
# 3. 없앨 수 있는 몬스터가 없다면 일을 끝냄

# 몬스터를 없애면 해당 칸은 빈칸
# 전투로봇이 한 칸 이동하는데에는 1초가 걸리고, 몬스터를 없애는 시간은 없다
# 전투 로봇은 본인의 레벨과 같은 수의 몬스터를 없앨 때마다 레벨이 상승

# 공간에 있는 몬스터와 전투로봇의 정보가 주어질 때, 전투 로봇이 일을 끝내기 전까지 걸린 시간

# 첫번째 줄에 격자판의 크기 n
# 두번째 줄부터 (n+1)번째 줄까지 공간에 대한 정보
# 0은 빈 곳, 1~6까지는 몬스터의 레벨, 9는 전투로봇

# BFS 로 각 몬스터의 위치 최단거리 구하기
# 거리, 행, 열 순으로 가장 가까운 몬스터 위치 구해 이동
# 1) 로봇 위치로부터 각각의 몬스터까지의 최단거리 구하기
# 2) 우선 순위가 높은 몬스터 위치 구하기
# 3) (거리, 행, 열) 순으로 가장 가까운 몬스터 선택

from collections import deque
NOT_EXISTS = (-1, -1)

# 격자판의 크기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 현재 로봇의 위치, 레벨
robot_pos = NOT_EXISTS
robot_level = 2
# 현재 레벨에서 잡은 몬스터의 수
caught_cnt = 0
queue = deque()

step = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
elapsed_time = 0

# 범위 안에 있는가
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 범위 안에 있고, 방문 안했고, 로봇 레벨보다 낮거나 같은가
def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] <= robot_level

# visited 배열을 초기화
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    # BFS 탐색
    while queue:
        curr_x, curr_y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            if can_go(new_x, new_y):
                queue.append((new_x, new_y))
                step[new_x][new_y] = step[curr_x][curr_y] + 1
                visited[new_x][new_y] = True


# best 위치를 새로운 위치로 바꿔줘야 하는지를 판단
def need_update(best_pos, new_pos):
    # 첫 도달 가능한 몬스터인 경우라면 update가 필요
    if best_pos == NOT_EXISTS:
        return True
    best_x, best_y = best_pos
    new_x, new_y = new_pos
    
    # 거리, 행, 열 순으로 더 작은 경우에만 고르기
    return (step[best_x][best_y], best_x, best_y) > (step[new_x][new_y], new_x, new_y)

# 가장 우선순위가 높은 몬스터가 있는 곳을 찾아 로봇을 이동
def move_robot():
    global robot_pos, robot_level, caught_cnt
    global elapsed_time
    
    # BFS 탐색을 위한 초기화
    initialize_visited()
    
	# Step1.
    # 로봇 위치로부터 각각의 몬스터 까지의 최단거리를 전부 구하기
    # 시작 로봇 위치로부터 BFS를 진행
    robot_x, robot_y = robot_pos
    visited[robot_x][robot_y] = True
    # 0은 빈 곳, 1~6까지는 몬스터의 레벨, 9는 전투로봇
    step[robot_x][robot_y] = 0
    queue.append(robot_pos)
    bfs()
    
	# Step2. 
    # 도달 할 수 있는 몬스터들 중가장 우선순위가 높은 몬스터의 위치를 구함
    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            # 도달이 불가능하거나 몬스터가 없거나 레벨이 같은 경우에는 패스
            if not visited[i][j] or not grid[i][j] or grid[i][j] == robot_level:
                continue            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos
    
	# Case 2-1.
    # 도달 가능한 몬스터가 있다면 로봇의 위치를 해당 위치로 옮김
    if best_pos != NOT_EXISTS:
        best_x, best_y = best_pos
        elapsed_time += step[best_x][best_y]
        grid[best_x][best_y] = 0
        robot_pos = best_pos
        caught_cnt += 1
        
        # 몬스터를 로봇 레벨만큼 잡게 되면 레벨이 1 올라감
        if caught_cnt == robot_level:
            robot_level += 1
            caught_cnt = 0
        return True

	# Case 2-2.
	# 도달 가능한 몬스터가 없다면 움직이는 것을 종료
    else:
        return False

# 처음 로봇의 위치
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            grid[i][j] = 0
            robot_pos = (i, j)
            robot_level = 2 
            caught_cnt = 0

# 없앨 수 있는 몬스터가 없어질 때까지 계속 반복
while True:
    is_moved = move_robot()
    if not is_moved:
        break

print(elapsed_time)

##################예제######################
"""
입력:
5
0 0 0 0 0
2 0 0 4 0
0 0 9 0 0
0 0 0 0 0
1 0 0 4 1

출력:
17
"""