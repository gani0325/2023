# codetree 참고함
# 정육면체 굴리기
# 0부터 9까지의 임의의 숫자가 그려진 n * m 격자판에 한 면이 1 * 1 크기인 정육면체
# 처음 정육면체의 각 면에는 0

# 칸에 쓰여져 있는 수가 0이면, 주사위의 바닥면에 쓰여져있는 수가 칸에 복사 (정육면체의 숫자는 변하지 않음)
# 칸에 쓰여져 있는 수가 0이 아니면 칸에 쓰여져있는 수가 정육면체 바닥면으로 복사되며, 해당 칸의 수는 0

# 정육면체의 초기 위치와 굴리는 방향이 주어질 때, 이동할 때마다 정육면체의 상단 면에 쓰여져 있는 숫자를 출력하는 프로그램

# 첫째줄에 말판의 세로 크기 n, 가로 크기 m, 정육면체의 처음 위치 x, y, 굴리기 횟수 k
# 정육면체의 처음 위치 x는 위부터 아래까지 0부터 n-1까지, y는 왼쪽에서 오른쪽까지 차례대로 번호
# 둘째줄부터 n+1번째 줄까지 지도에 쓰여져있는 수
# 마지막 줄에는 굴리기 방향 (1이상 4이하의 숫자 -> 동쪽, 서쪽, 북쪽, 남쪽)
# 말판의 범위를 벗어나는 방향이 주어졌을 경우에는 굴리기를 수행하지 않음

# 주사위의 마주보는 두면 숫자의 합은 항상 7

FACE_NUM = 6
OUT_OF_GRID = (-1, -1)

# 말판의 세로 크기 n, 가로 크기 m, 정육면체의 처음 위치 x, y, 굴리기 횟수 k
n, m, x, y, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split()))for _ in range(n)]
movements = list(map(int, input().split()))

# 주사위가 놓여있는 상태 
up, front, right = 1, 2, 3

# 주사위의 각 면마다 적혀 있는 숫자
dices = [0 for _ in range(FACE_NUM + 1)]

# 격자 안에 있는지를 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 해당 방향으로 이동했을 때의 다음 위치
# 이동이 불가능할 경우 OUT_OF_GRID를 반환
def next_pos(x, y, move_dir):
    dxs, dys = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    return (nx, ny) if in_range(nx, ny) else OUT_OF_GRID

def simulate(move_dir):
    global x, y
    global up, front, right
    
    # move_dir 방향으로 굴렸을 때의 격자상의 위치
    nx, ny = next_pos(x, y, move_dir)
    # 굴리는게 불가능한 경우라면 패스
    if (nx, ny) == OUT_OF_GRID:
        return
    
    # 위치를 이동합
    x, y = nx, ny
    
    # 주사위가 놓여있는 상태를 조정
    # up, front, right = 1, 2, 3
    if move_dir == 1: # 동쪽
        up, front, right = 7 - right, front, up
    elif move_dir == 2: # 서쪽
        up, front, right = right, front, 7 - up
    elif move_dir == 3: # 북쪽
        up, front, right = front, 7 - up, right
    else: # 남쪽
        up, front, right = 7 - front, up, right
    
    # 주사위 & 바닥에 적혀있는 숫자를 변경
    bottom = 7 - up
    
    # 칸에 쓰여있는 수가 0이면 주사위 숫자가 복사
    if grid[x][y] == 0:
        grid[x][y] = dices[bottom]
    # 칸에 0이 아닌 수가 적혀있다면, 주사위에 숫자가 쓰여지고
    # 해당 칸은 0
    else:
        dices[bottom] = grid[x][y]
        grid[x][y] = 0
    
    # 출력
    print(dices[up])
    
# 시뮬레이션 진행
for move_dir in movements:
    simulate(move_dir)

##################예제######################
"""
입력:
3 4 1 1 8
1 2 3 4
5 0 6 7
8 9 0 0
4 1 3 3 2 4 4 2

출력:
0
0
0
0
0
0
2
3
"""