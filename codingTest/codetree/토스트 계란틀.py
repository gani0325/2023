# codetree 참고함
# 토스트 계란틀
# n * n개의 격자에 1 * 1 크기의 계란틀
# 각각의 계란틀에 담긴 계란의 양이 주어지며 계란틀은 정사각형 형태
# 계란틀을 이루는 4개의 선은 분리가 가능

# 계란틀 규칙
# 1. 계란의 양이 차이나지 않게 하기 위해 하나의 선을 맞댄 두 계란틀의 계란의 양의 차이가 L 이상 R 이하 -> 계란틀의 해당 선 분리
# 2. 모든 계란틀에 대해 검사를 실시하고 위의 규칙에 해당하는 모든 계란틀의 선을 분리
# 3. 선의 분리를 통해 합쳐진 계란틀의 계란은 하나로 합치고 이후에 다시 분리
# 4. 합쳤다 다시 분리한 이후의 각 계란틀별 계란의 양은 (합쳐진 계란의 총 합)/(합쳐진 계란틀의 총 개수) (편의상 소숫점은 버림)

# n * n 격자의 계란틀에 있는 계란의 양이 주어질 때, 계란의 이동이 몇 번 일어나는지를 구하는 프로그램

# 첫번째 줄에 총 칸의 크기 n, 계란 이동의 범위의 최솟값 L, 계란 이동 범위의 최댓값 R
# 두번째 줄부터 (n+1)번째 줄까지 각 칸의 계란의 양

from collections import deque

# 칸의 크기 n, 계란 이동의 범위의 최솟값 L, 계란 이동 범위의 최댓값 R
n, L, R = map(int, input().split())
egg = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
egg_group = []
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, curr_egg):
    if not in_range(x, y):
        return False
    egg_diff = abs(egg[x][y] - curr_egg)
    # 계란 이동 범위 안이고, 방문 안했다면
    return not visited[x][y] and L <= egg_diff and egg_diff <= R 

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
            
            # L, R 사이인 경우에만 합쳐짐
            if can_go(new_x, new_y, egg[curr_x][curr_y]):
                queue.append((new_x, new_y))
                egg_group.append((new_x, new_y))
                visited[new_x][new_y] = True

# 계란들을 합침
def merge_eggs():
    sum_of_eggs = sum([
        egg[x][y] 
        for x, y in egg_group
    ])

    for x, y in egg_group:
        egg[x][y] = sum_of_eggs // len(egg_group)

# 조건에 맞게 계란의 양을 바꿔줌
def move_eggs():
    global egg_group
    
    # BFS 탐색을 위한 초기화 작업
    initialize_visited()
    
    is_changed = False
    
    # 아직 방문하지 못한 칸에 대해 BFS 탐색을 통해 합쳐질 계란들을 찾아냄
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 합쳐질 계란 목록을 담을 곳을 초기화
                egg_group = []                
                queue.append((i, j))
                egg_group.append((i, j))
                visited[i][j] = True

                bfs()
                
                # 계란의 이동이 한번이라도 일어났는지를 확인
                if len(egg_group) > 1:
                    is_changed = True
                
                # (i, j)와 관련이 있는 계란들을 합침
                merge_eggs()
    
    return is_changed


move_cnt = 0

# 이동이 더 이상 필요 없을 때까지
# 계란의 이동을 반복합니다.
while True:
    is_changed = move_eggs()
    if not is_changed:
        break
    move_cnt += 1

print(move_cnt)

##################예제######################
"""
입력:
3 15 24
20 25 40
30 50 40
10 30 45

출력:
1
"""