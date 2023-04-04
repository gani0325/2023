# codetree 참고함
# 생명과학부 랩 인턴
# n * m 격자판에서 움직이는 곰팡이를 채취하는 일
# 빨간색 숫자는 곰팡이의 크기, 파란색 숫자는 속력

# 1. 승용이는 첫번째 열부터 탐색을 시작
# 2. 해당 열의 위에서 아래로 내려가며 탐색할 때 제일 빨리 발견한 곰팡이를 채취 (해당 칸은 빈칸)
# 3. 해당 열에서 채취가 끝나고 나면 곰팡이는 이동을 시작
# 4. 주어진 방향과 속력으로 이동하며 벽에 도달하면 반대로 방향을 바꾸고 속력 유지한 채로 이동 (방향을 바꿀 때 시간 걸리지 않음)
# 5. 모든 곰팡이가 이동을 끝낸 후에 한 칸에 곰팡이가 두마리 이상이면 크기가 큰 곰팡이가 다른 곰팡이를 모두 잡아먹음
# 6. 이 모든 과정은 1초가 걸리며 이후 승용이는 오른쪽 열로 이동해서 위의 과정을 반복

# 해당 격자판에 있는 모든 열을 검사했을 때, 채취한 곰팡이 크기의 총합을 구하는 프로그램

# 첫번째 줄에 격자판의 크기 n, m과 곰팡이의 수 k
# 두번째 줄부터 k+1번째 줄까지 곰팡이의 정보 x, y, s, d, b
# x, y는 곰팡이의 위치, s는 1초동안 곰팡이가 움직이는 거리, d는 이동 방향 (1 위, 2 아래, 3 오른쪽, 4 왼쪽), b는 곰팡이의 크기

# mold_size, dist, move_dir
BLANK = (-1, -1, -1)

# 격자판의 크기 n, m과 곰팡이의 수 k
n, m, k = map(int, input().split())
# 곰팡이 정보
mold = [[BLANK for _ in range(m)] for _ in range(n)]
next_mold = [[BLANK for _ in range(m)] for _ in range(n)]
ans = 0

# 격자판에 있는가
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def collect(col):
    global ans
    for row in range(n):
        if mold[row][col] != BLANK:
            mold_size, _, _ = mold[row][col]
            
            ans += mold_size
            mold[row][col] = BLANK
            break

def get_next_pos(x, y, dist, move_dir):
    # 문제에서 주어진 순서인 위, 아래, 오른쪽, 왼쪽
    dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]
    
    # dist번 한 칸씩 이동
    for _ in range(dist):
        next_x, next_y = x + dxs[move_dir], y + dys[move_dir]
        # 현재 방향으로 이동했다 했을 때 만약 격자를 벗어나지 않는다면, 그대로 이동
        if in_range(next_x, next_y):
            x, y = next_x, next_y
        # 만약 격자를 벗어나게 된다면 방향을 반대로 바꾸고 한 칸 이동
        else:
            # d는 이동 방향 (1 위, 2 아래, 3 오른쪽, 4 왼쪽)
            move_dir = move_dir + 1 if move_dir % 2 == 0 else move_dir - 1
            x, y = x + dxs[move_dir], y + dys[move_dir]
    
    return (x, y, move_dir)

# (x, y) 위치에 있는 곰팡이를 이동
def move(x, y):
    mold_size, dist, move_dir = mold[x][y]
    next_x, next_y, next_dir = get_next_pos(x, y, dist, move_dir)
    
    new_mold = (mold_size, dist, next_dir)
    
    # 현재 곰팡이의 크기가 해당 위치에 있던 것 보다 더 큰 경우에만 곰팡이 정보 적음
    # 그렇지 않은 경우라면 충돌시 사라지게 될 곰팡이이므로 무시
    if new_mold > next_mold[next_x][next_y]:
        next_mold[next_x][next_y] = new_mold

def move_all():
    # next_mold 값을 전부 빈칸으로 초기화
    for i in range(n):
        for j in range(m):
            next_mold[i][j] = BLANK
    
    # 곰팡이를 한번씩 이동
    for i in range(n):
        for j in range(m):
            if mold[i][j] != BLANK:
                move(i, j)
    
    # next_mold 값을 mold에 옮김
    for i in range(n):
        for j in range(m):
            mold[i][j] = next_mold[i][j]

def simulate(col):
    # 해당 열에 있는 곰팡이를 채취
    collect(col)
    
    # 곰팡이들을 전부 움직임
    move_all()

for _ in range(k):
    # x, y는 곰팡이의 위치, s는 1초동안 곰팡이가 움직이는 거리, d는 이동 방향 (1 위, 2 아래, 3 오른쪽, 4 왼쪽), b는 곰팡이의 크기
    x, y, s, d, b = map(int, input().split())
        
    # 위, 아래 방향으로 움직이는 경우 2n - 2번 움직이면 다시 제자리로 돌아오게 되므로
    # 움직여야 할 거리를 2n - 2로 나눴을 때의 나머지 만큼만 움직이게 하면 최적화가 가능
    if d <= 2:
        s %= (2 * n - 2)
    # 왼쪽, 오른쪽 방향으로 움직이는 경우 2m - 2번 움직이면 다시 제자리로 돌아오게 되므로
    # 움직여야 할 거리를 2m - 2로 나눴을 때의 나머지 만큼만 움직이게 하면 최적화가 가능
    else:
        s %= (2 * m - 2)

    # tuple에 넣을 때 곰팡이 크기 정보를 먼저 넣어, 후에 곰팡이끼리 충돌이 일어날 경우
    # 크기부터 비교하여 최대인 곰팡이를 쉽게 판단
    mold[x - 1][y - 1] = (b, s, d - 1)
    
# 한 칸씩 이동하면서 곰팡이를 채취
for col in range(m):
    simulate(col)

print(ans)

##################예제######################
"""
입력:
5 6 5
2 1 5 3 3
2 5 5 2 2
3 2 0 3 1
5 1 1 4 5
5 3 4 1 4

출력:
11
"""