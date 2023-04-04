# codetree 참고함
# 이상한 체스
# 1번째 말은 한 방향으로만 이동 가능
# 각각의 말들은 네 방향 중 한 가지 방향을 선택, 방향에 따라 이동할 수 있는 격자의 범위 다름

# 체스판에 놓인 말들의 방향을 적절히 설정하여 갈 수 없는 격자의 크기를 최소화

# 말의 이동 특징
# 1. 본인의 말은 뛰어넘어서 지나갈 수 있음
# 2. 상대편의 말은 뛰어넘어서 지나갈 수 없음
# (갈 수 없는 격자의 크기를 계산할 때 상대편 말이 있는 격자는 계산하지 않음)

# 첫째 줄에 체스판의 세로 크기 n과 가로 크기 m
# 두번째 줄부터 (n+1)번째 줄까지 체스판에 있는 (1~5) 자신의 말, (6) 상대편의 말
# 1 ≤ n, m ≤ 8 + 자신의 말의 개수는 최대 8개를 넘지 않는다고 가정

# 이동 가능한 방향이 시계방향으로 90도 회전

import sys
min_area = sys.maxsize

# 체스판의 세로 크기 n과 가로 크기 m
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess_pieces = [(i, j) for i in range(n) for j in range(m) if 1 <= board[i][j] and board[i][j] <= 5]

# 말들의 방향
piece_dir = [[0 for _ in range(m)] for _ in range(n)]

# 자신의 말로 갈 수 있는 영역을 표시
visited = [[False for _ in range(m)] for _ in range(n)]

# 말의 종류마다 북동남서 방향으로 이동이 가능한지 표시
can_move = [
    [],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 움직일 수 있는 곳인지 여부를 확인 (체스판 안이고, 상대방 말이 아니면)
def can_go(x, y):
    return in_range(x, y) and board[x][y] != 6

# (start_x, start_y)에서 해당 타입의 말이 특정 방향을 바라보고 있을 때 갈 수 있는 곳들을 전부 표시
def fill(start_x, start_y, piece_num, face_dir):
    # 북동남서 순으로 방향을 설정
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    for i in range(4):
        # 해당 말이 움직일 수 있는 방향인지를 확인 (움직일 수 없다면 pass)
        if not can_move[piece_num][i]:
            continue
        
        # 갈 수 있다면, 끝날때까지 계속 진행
        # 방향은 face_dir만큼 시계방향으로 회전했을 때를 기준으로 움직임
        x, y = start_x, start_y
        move_dir = (i + face_dir) % 4;
        while True:
            visited[x][y] = True
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
            if can_go(nx, ny):
                x, y = nx, ny
            else:
                break

# n 개의 체스 말의 방향이 정해졌을 때 이동할 수 없는 영역의 넓이를 반환
def get_area():
    # visited 배열을 초기화
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
    
    for x, y in chess_pieces:
        # 해당 말이 정해진 방향에 있을 때 갈 수 있는 곳들을 전부 표시
        fill(x, y, board[x][y], piece_dir[x][y])
    
    area = 0
    for i in range(n) :
        for j in range(m) :
            if visited[i][j] == 0 and board[i][j] != 6 :
                area += 1
    return area

def search_min_area(cnt):
    global min_area
    
    # 자신의 말들의 방향이 전부 결정되었을 때, 갈 수 없는 넓이를 계산하여 갱신
    if cnt == len(chess_pieces):
        min_area = min(min_area, get_area())
        return

    # cnt 말의 방향을 설정
    piece_x, piece_y = chess_pieces[cnt]
    
    for i in range(4):
        piece_dir[piece_x][piece_y] = i
        search_min_area(cnt + 1)

search_min_area(0)
print(min_area)

##################예제######################
"""
입력:
5 4
0 0 0 0
0 2 0 6
0 0 0 5
0 1 0 0
0 0 0 0

출력:
8
"""