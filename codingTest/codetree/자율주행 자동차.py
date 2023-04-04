# codetree 참고함
# 자율주행 자동차
# n * m 크기의 도로에 1 * 1 크기의 자율주행 자동차

# 1. 현재 방향을 기준으로 왼쪽 방향으로 한 번도 간 적이 없다면 좌회전해서 해당 방향으로 1 칸 전진
# 2. 왼쪽 방향이 인도거나 이미 방문한 도로인 경우 좌회전 + 1번 과정을 시도
# 3. 2번에 대해 4방향 모두 확인하였으나 전진하지 못한 경우, 바라보는 방향에서 한 칸 후진 + 1번 과정을 시도
# 4. 번 과정을 시도하려 했지만 뒷 공간이 인도여서 후진조차 하지 못한다면 작동을 멈춤

# 자율주행 자동차가 작동을 멈췄을 때 거쳐갔던 도로의 총 면적 구하는 프로그램 (처음 위치 도로도 함께 계산)

# 좌회번 하므로 반시계 방향으로 90도 회전
# 첫째 줄에 도로의 세로 크기 n과 가로 크기 m
# 둘째 줄에 자율주행 자동차의 초기 위치 (x, y), 바라보는 방향 d (0부터 3 -> 북쪽, 동쪽, 남쪽, 서쪽)
# 자동차의 처음 위치 x는 위쪽에서부터 아래쪽까지 0부터 n-1까지, y는 왼쪽에서 오른쪽까지
# 셋째줄부터 n+2번째 줄까지는 도로의 상태 (도로는 0, 인도는 1)

# n * m 크기의 도로
n, m = map(int, input().split())
# 자동차의 초기 위치 (x, y), 바라보는 방향 d
curr_x, curr_y, curr_dir = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 이미 방문한 적이 있었는지를 표시
visited = [[False for _ in range(m)] for _ in range(n)]

# 해당 위치로 갈 수 있는지 확인 (배열 안이고, 방문한적이 없다면)
def can_go(x, y):
    return not grid[x][y] and not visited[x][y]

# 움직인 경우 True, 아닌 경우 False를 반환
def simulate():
    global curr_x, curr_y, curr_dir
    
    # 방문 여부를 체크
    visited[curr_x][curr_y] = True

    # 0부터 3까지 차례대로 북동남서 순 입니다.
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    # Step1. 현재 방향을 시작으로 4방향을 전부 탐색
    for _ in range(4):
        # 현재 방향을 기준으로 왼쪽 방향으로 갈 수 있는지 확인
        left_dir = (curr_dir - 1 + 4) % 4
        next_x = curr_x + dxs[left_dir]
        next_y = curr_y + dys[left_dir]
        
        # Case1-1. 왼쪽 방향으로 갈 수 있다면 1칸 전진
        if can_go(next_x, next_y):
            curr_x, curr_y = next_x, next_y
            curr_dir = left_dir
            return True
        
        # Case1-2. 왼쪽 방향으로 갈 수 없다면 좌회전, 그 다음 방향을 시도
        else:
            curr_dir = left_dir

    # Step2. 만약 4곳 모두 갈 곳이 없었다면 한 칸 후진을 시도
    back_x = curr_x - dxs[curr_dir]
    back_y = curr_y - dys[curr_dir]
    
    # Case2-1. 후진이 가능하다면 그대로 진행
    if not grid[back_x][back_y]:
        curr_x, curr_y = back_x, back_y
        return True
    # Case2-2. 후진이 불가능하다면 움직일 수 없음
    else:
        return False

# 계속 움직이기
while True:
    # 조건에 맞춰 움직이기
    moved = simulate()

    # 움직이지 못했다면 종료
    if not moved:
        break

# 움직인 영역을 계산
ans = 0
for i in range(n) :
    for j in range(m) :
        if visited[i][j] == True :
            ans += 1

# 출력
print(ans)

##################예제######################
"""
입력:
5 5
1 1 0
1 1 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 0 0 1
1 1 1 1 1

출력:
8
"""