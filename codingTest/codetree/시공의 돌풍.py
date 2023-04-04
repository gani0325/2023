# codetree 참고함
# 시공의 돌풍
# n * m 크기의 격자칸으로 이루어진 방 안에 먼지가 가득
# 먼지는 각 칸에 구분이 되게 쌓여있으며, 방 안의 먼지를 자동으로 치워주는 기계 시공의 돌풍을 사용해서 청소
# 시공의 돌풍은 항상 1번 열에 설치, 크기는 두 칸을 차지

# 1초 동안 방에서 일어나는 일
# 1. 먼지가 인접한 4방향의 상하좌우 칸으로 확산
# a. 인접한 방향에 시공의 돌풍이 있거나, 방의 범위를 벗어난다면 해당 방향으로는 확산이 일어나지 않음
# b. 확산되는 양은 원래 칸의 먼지의 양에 5를 나눈 값이며, 편의상 소숫점은 버림
# c. 각 칸에 확산될 때마다 원래 칸의 먼지의 양은 확산된 먼지만큼 줄어듦
# d. 확산된 먼지는 방에 있는 모든 먼지가 확산을 끝낸 다음에 해당 칸에 더해짐

# 2. 시공의 돌풍이 청소를 시작
# a. 시공의 돌풍의 윗칸에서는 반시계 방향으로 바람을 일으키며, 아랫칸에서는 시계 방향으로 바람을 일으킴
# b. 바람이 불면 먼지가 바람의 방향대로 모두 한 칸씩 이동
# c. 시공의 돌풍에서 나온 바람은 먼지가 없는 청정한 바람, 시공의 돌풍으로 들어간 먼지는 사라짐

# 방의 정보가 주어질 때 t초 후에 총 먼지의 양을 출력하는 프로그램

# 첫번째 줄에는 방의 크기 n, m과 시간 t
# 두번째 줄부터 n개의 줄까지는 방안에 있는 먼지의 양
# 시공의 돌풍이 설치되어 있는 칸은 -1 (항상 맨 왼쪽에 위치), 두 칸을 차지
# (시공의 돌풍은 맨 윗 행과 맨 아랫 행과 적어도 두 칸 이상 떨어져 있음)

WINDBLAST = -1

# 방의 크기 n, m과 시간 t
n, m, t = map(int, input().split())

dust = [list(map(int, input().split())) for _ in range(n)]
next_dust = [[0 for _ in range(m)] for _ in range(n)]

# 방 안에 있는가
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m
# 방안에 있고 돌풍이 있는 곳이 아닌가
def can_spread(x, y):
    return in_range(x, y) and dust[x][y] != WINDBLAST

# (x, y)에서 인접한 4방향으로 확산
def spread(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    curr_dust = dust[x][y]
    
    # 인접한 4방향으로 확산
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        # 격자 안이면서, 시공의 돌풍이 없는 곳으로만 확산이 가능
        if can_spread(nx, ny):
            next_dust[nx][ny] += curr_dust // 5
            dust[x][y] -= curr_dust // 5

# 먼지 확산
def diffusion():
    # next_dust 값을 0으로 초기화
    for i in range(n):
        for j in range(m):
            next_dust[i][j] = 0
    
    # 시공의 돌풍을 제외한 위치에서만 확산
    for i in range(n):
        for j in range(m):
            if dust[i][j] != WINDBLAST:
                spread(i, j)
    
    # next_dust값을 확산 후 남은 dust에 더함
    for i in range(n):
        for j in range(m):
            dust[i][j] += next_dust[i][j]

# 위로 시계방향 청소 시작
def counter_clockwise_roration(start_row, start_col, end_row, end_col):
    # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장
    temp = dust[start_row][start_col]

    # Step1-2. 직사각형 가장 위 행을 왼쪽으로 한 칸씩 shift 
    for col in range(start_col, end_col):
        dust[start_row][col] = dust[start_row][col + 1]
    
    # Step1-3. 직사각형 가장 오른쪽 열을 위로 한 칸씩 shift 
    for row in range(start_row, end_row):
        dust[row][end_col] = dust[row + 1][end_col]
    
    # Step1-4. 직사각형 가장 아래 행을 오른쪽으로 한 칸씩 shift 
    for col in range(end_col, start_col, -1):
        dust[end_row][col] = dust[end_row][col - 1]
    
    # Step1-5. 직사각형 가장 왼쪽 열을 아래로 한 칸씩 shift 
    for row in range(end_row, start_row, -1):
        dust[row][start_col] = dust[row - 1][start_col]

    # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 아래 칸에 넣습니다. 
    dust[start_row + 1][start_col] = temp

# 아래로 반시계방향 청소 시작
def clockwise_rotation(start_row, start_col, end_row, end_col):
    # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장
    temp = dust[start_row][start_col]

    # Step1-2. 직사각형 가장 왼쪽 열을 위로 한 칸씩 shift 
    for row in range(start_row, end_row):
        dust[row][start_col] = dust[row + 1][start_col]
    
    # Step1-3. 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 shift 
    for col in range(start_col, end_col):
        dust[end_row][col] = dust[end_row][col + 1]

    # Step1-4. 직사각형 가장 오른쪽 열을 아래로 한 칸씩 shift 
    for row in range(end_row, start_row, -1):
        dust[row][end_col] = dust[row - 1][end_col]
    
    # Step1-5. 직사각형 가장 위 행을 오른쪽으로 한 칸씩 shift 
    for col in range(end_col, start_col, -1):
        dust[start_row][col] = dust[start_row][col - 1]

    # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 오른쪽 칸에 넣습니다. 
    dust[start_row][start_col + 1] = temp

def cleaning():
    # 돌풍의 행
    windblast_rows = [i for i in range(n) if dust[i][0] == WINDBLAST]
    # 돌풍 시작점이 (0, 0), 끝나는 점이 (돌풍 행, m-1)
    counter_clockwise_roration(0, 0, windblast_rows[0], m - 1)
    # 돌풍 시작점이 (행, 0), 끝나는 점이 (n-1, m-1)
    clockwise_rotation(windblast_rows[1], 0, n - 1, m - 1)
    
    # 돌풍 보정
    dust[windblast_rows[0]][0] = dust[windblast_rows[1]][0] = -1
    dust[windblast_rows[0]][1] = dust[windblast_rows[1]][1] = 0

def simulate():
    # 확산
    diffusion()
    # 시공의 돌풍이 청소를 진행
    cleaning()

# 총 t번 시뮬레이션을 진행
for _ in range(t):
    simulate()

ans = sum([
    dust[i][j]
    for i in range(n)
    for j in range(m)
    if dust[i][j] != WINDBLAST
])

print(ans)

##################예제######################
"""
입력:
6 7 1
10 15 17 4 50 10 16
30 16 2 4 15 21 27
-1 11 31 51 1 22 47
-1 34 15 21 61 15 21
31 15 20 13 41 43 4
31 12 15 20 15 20 14

출력:
810
"""