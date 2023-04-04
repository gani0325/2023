# codetree 참고함
# 병원 거리 최소화하기
# 사람, 병원 혹은 빈 칸으로 이루어져 있는 n×n 크기의 도시
# 두 격자 (x1, y1), (x2, y2) 사이의 거리는 |x2 - x1| + |y2 - y1|

# 운영상의 이유로 m개의 병원만을 남겨두고 나머지를 폐업해야 할 때
# 남은 m개의 병원에 대한 각 사람들의 병원 거리의 총 합이 최소

# 첫 번째 줄에는 n과 m
# 두 번째 줄부터 (n+1)번째 줄까지는 빈 칸인 경우 0, 사람인 경우 1, 병원인 경우 2
# m 개의 병원을 고르는게 불가능한 입력은 주어지지 않는다고 가정

# 모든 병원의 조합에 대해 병원 거리 합 구한 후 최솟값 찾기

import sys

MAX_HOSPITAL = 13
INT_MAX = sys.maxsize

# n×n 크기의 도시, 남은 m개의 병원
n, m = map(int, input().split())
given_map = [list(map(int, input().split())) for _ in range(n)]
# 빈 칸인 경우 0, 사람인 경우 1, 병원인 경우 2
people = [(i, j) for i in range(n) for j in range(n) if given_map[i][j] == 1]
hospitals = [(i, j) for i in range(n) for j in range(n) if given_map[i][j] == 2]
visited = [False for _ in range(MAX_HOSPITAL)]

min_distance = INT_MAX

# 사람과 병원 사이의 거리를 구하여 반환
def get_distance(person, hospital):
    px, py = person
    hx, hy = hospital
    return abs(px - hx) + abs(py - hy)


# m개의 병원이 선택됐을 때 각 사람의 병원 거리에 대한 합을 반환
def get_curr_min_distance():
    curr_min_distance = 0
    
    # 각 사람에 대하여 가장 가까운 병원의 거리
    for per in people:
        single_min = min([
            get_distance(per, hospital)
            for i, hospital in enumerate(hospitals)
            if visited[i]
        ])
        curr_min_distance += single_min
    
    return curr_min_distance

def search_min_distance(cnt, last_idx):
    global min_distance
    
    # m개의 병원이 선택되었을 경우 병원 거리의 총합
    if cnt == m:
        min_distance = min(min_distance, get_curr_min_distance())
        return
    
    # 뽑을 수 있는 병원의 후보들을 탐색
    for i in range(last_idx + 1, len(hospitals)):
        visited[i] = True
        search_min_distance(cnt  + 1, i)
        visited[i] = False

search_min_distance(0, -1)
print(min_distance)

##################예제######################
"""
입력:
3 1
0 1 0
0 2 2
0 1 0

출력:
2
"""