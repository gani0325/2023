# codetree 참고함
# 바이러스 백신
# N×N 크기의 도시에 병원과 벽을 제외한 모든 지역에 바이러스가 생김
# 모든 병원에서 백신을 공급할 수는 없어, M개의 병원을 적절히 골라 최대한 빨리 바이러스를 없애자
# M개의 병원을 고르게 되면 매초마다 상하좌우로 인접한 지역 중 벽을 제외한 지역에 백신 공급 (그 자리에 있던 바이러스 사라짐)

# M개의 병원을 적절히 골라 바이러스를 전부 없애는데 걸리는 시간 중 최소 시간을 구하는 프로그램을 작성
# 모든 바이러스를 없앨 수 있는 방법이 없다면 −1을 출력

# 첫째 줄에는 N과 M
# 둘째 줄 부터는 N개의 줄에 걸쳐 각 행의 상태에 해당하는 N개의 숫자 (0은 바이러스, 1은 벽, 2는 병원)
# 총 병원의 수가 항상 M보다 크거나 같고, 10을 넘지 않음

# BFS 사용하여 거리가 가장 가까운 정점부터 큐에서 나오므로, 가장 가까운 병원까지의 거리가 가까운 바이러스 선택 -> 최단거리

from collections import deque
import sys

INT_MAX = sys.maxsize

# N×N 크기의 도시, M개의 병원
n, m = map(int, input().split())
citis = [list(map(int, input().split())) for _ in range(n)]
hospitals = []
selected_hos = []

# bfs
queue = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
step = [[False for _ in range(n)] for _ in range(n)]
ans = INT_MAX

# 범위가 격자 안에 들어가는지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 범위를 벗어나지 않으면서, 벽이 아니고, 방문한적이 없어야함
def can_go(x, y):
    return in_range(x, y) and citis[x][y] != 1 and not visited[x][y]

# queue에 새로운 위치를 추가하고 방문 여부를 표시
# 시작점으로부터의 최단거리 값도 갱신
def push(x, y, new_step):
    queue.append((x, y))        # 새로운 위치를 추가
    visited[x][y] = True        # 방문 여부를 표시
    step[x][y] = new_step       # 최단거리 값

# visited, step 배열을 초기화
def initialize():
    for i in range(n):
        for j in range(n):
            visited[i][j] = step[i][j] = 0

# BFS를 통해 선택된 병원들로부터 가장 거리가 먼 바이러스까지의 거리 구하기
def find_max_dist():
    while queue:
        # queue에서 가장 먼저 들어온 원소를 뺌 (가장 가까운거징)
        x, y = queue.popleft()        
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        
        # queue에서 뺀 원소의 위치를 기준으로 4 방향을 확인
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            
            # 더 갈 수 있는 곳이라면 Queue에 추가
            if can_go(new_x, new_y):
                # 최단 거리는 이전 최단거리에 1이 증가
                push(new_x, new_y, step[x][y] + 1)

    # 바이러스들 까지의 거리들 중 가장 먼 거리를 기록
    max_dist = 0
    
    for i in range(n):
        for j in range(n):
            # 바이러스인 경우에만 거리를 갱신
            if citis[i][j] == 0:
                if visited[i][j]:
                    max_dist = max(max_dist, step[i][j])
                # 만약 선택한 병원 조합으로는 해당 바이러스에 도달이 불가능하다면
                # 도달이 불가능 하다는 표시로 INT_MAX
                else:
                    max_dist = INT_MAX
    return max_dist

# 선택된 병원으로부터 모든 바이러스를 없애기 위해 걸리는 시간을 계산
def elapsed_time_to_kill_all_virus():
    # BFS를 다시 돌리기 전에 visited, step 배열을 초기화
    initialize()
    
    # 선택된 병원들을 시작으로 하여 BFS를 한 번 돌림
    for i in range(len(selected_hos)):
        x, y = selected_hos[i]
        push(x, y, 0)
    
    max_elapsed_time = find_max_dist()      # 바이러스 중 가장 먼 거리
    return max_elapsed_time

# Backtracking을 이용하여 m개의 병원을 전부 선택 -> 모든 바이러스를 없애는 데 걸리는 시간 중 최소 시간
def find_min_time(curr_idx, cnt):
    global ans
    
    if cnt == m:
        # 선택된 병원으로부터 모든 바이러스를 없애기 위해 걸리는 시간을 계산하여 답보다 더 좋은 경우 갱신
        ans = min(ans, elapsed_time_to_kill_all_virus())
        return
    
    if curr_idx == len(hospitals):
        return
    
    find_min_time(curr_idx + 1, cnt)
    selected_hos.append(hospitals[curr_idx])
    find_min_time(curr_idx + 1, cnt + 1)
    selected_hos.pop()
    
# Backtracking을 선택할 병원 index 기준으로 쉽게 돌리기 위해 병원 위치만 따로 저장
for i in range(n):
    for j in range(n):
        if citis[i][j] == 2:
            hospitals.append((i, j))

# 최소 시간을 구합니다.
find_min_time(0, 0)
if ans == INT_MAX:
    ans = -1
    
print(ans)

##################예제######################
"""
입력:
6 3
2 1 2 0 1 1
0 0 0 1 0 1
1 1 0 0 2 0
1 0 0 1 0 1
1 0 0 0 0 1
1 1 2 1 0 1

출력:
3
"""