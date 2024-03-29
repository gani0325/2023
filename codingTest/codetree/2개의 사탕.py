# codetree 참고함
# 2개의 사탕
# 상자 안에는 사탕이 지나가지 못하도록 하는 장애물이 여러 개 있고, 사탕이 밖으로 빠져 나올 수 있는 구멍이 딱 하나
# 빨간색 사탕을 밖으로 빼야 하지만, 파란색 사탕이 밖으로 나와서는 안됨 (동시에 둘 다 나오는 것도 안됨)
# 빨간색 사탕을 밖으로 빼내기 위해 기울여야 하는 최소 횟수 (10번 이내에 빨간색 사탕을 밖으로 빼내는 것이 불가능, −1을 출력)

# N X M 상자
N, M = tuple(map(int, input().split()))

# '.', ‘#', ‘B’, ‘R’, 'O’ = 빈 칸, 장애물, 파란색 사탕, 빨간색 사탕, 출구
BLANK = 0
BLOCK = 1
EXIT = 2
RED = 3
BLUE = 4

# 빨간색, 파란색 사탕의 위치를 저장할 변수
red_pos = (0, 0)
blue_pos = (0, 0)
# 편의상 절대 맵 안에서는 될 수 없는 위치인 (n, m)로 설정
OUT_OF_MAP = (N, M)

ans = 11

# 파란색이 맵에 남아있는지 판단
def blue_exist():
    return blue_pos != OUT_OF_MAP
# 빨간색이 맵에 남아있는지 판단
def red_exist():
    return red_pos != OUT_OF_MAP

# 상자를 move_dir방향으로 기울였을 때
# 파란색 보다 빨간색을 무조건 먼저 움직여야 하는지 판단
def red_must_first(move_dir):
    (rx, ry), (bx, by) = red_pos, blue_pos
    
    # 상자가 위,
    # 두 사탕의 열의 위치가 같으며, 빨간색의 행의 위치가 더 작을때
    if move_dir == 0:
        return (ry == by and rx < bx)

    # 상자가 아래,
    # 두 사탕의 열의 위치가 같으며, 빨간색의 행의 위치가 더 클 때
    elif move_dir == 1:
        return (ry == by and rx > bx)

    # 상자가 왼쪽,
    # 두 사탕의 행의 위치가 같으며, 빨간색의 열의 위치가 더 작을때
    elif move_dir == 2:
        return (rx == bx and ry < by)
    
    # 상자가 오른쪽,
    # 두 사탕의 행의 위치가 같으며, 빨간색의 열의 위치가 더 클 때
    else:
        return (rx == bx and ry > by)

# (x, y)로 진행이 가능한지 판단
# 더 진행하기 위해서는 해당 위치에 벽이나 사탕이 없어야 함
def can_go(x, y):
    return a[x][y] != BLOCK and (x, y) != red_pos and (x, y) != blue_pos

# pos(x, y)에서 move_dir 방향으로 이동했을 때 최종적으로 도착하는 위치를 반환
def get_destination(pos, move_dir):
    # 위, 아래, 왼쪽, 오른쪽
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    curr_x, curr_y = pos
    nx, ny = curr_x + dxs[move_dir], curr_y + dys[move_dir]
    
    # 그 다음 위치가 가로막혀 있다면 현재 위치가 최종 도착지
    if not can_go(nx, ny):
        return pos
    
    # 그 다음 위치가 출구라면 사탕은 맵 밖으로 나감
    if a[nx][ny] == EXIT:
        return OUT_OF_MAP
    
    # 아직 더 이동할 수 있다면, 그 다음 위치에서 move_dir 방향으로
    # 이동했을 때의 최종 도착지를 찾아 반환
    return get_destination((nx, ny), move_dir)

# move_dir 0, 1, 2, 3는 각각 상하좌우를 의미
def tilt(move_dir):
    global red_pos, blue_pos
    
    # dir 방향으로 봤을 때, 파란색 보다 
    # 빨간색을 무조건 먼저 움직여야할 상황인지 판단
    if red_must_first(move_dir):
        # 빨간색, 파란색 순서로 움직
        red_pos = get_destination(red_pos, move_dir)
        blue_pos = get_destination(blue_pos, move_dir)
    else:
        # 파란색, 빨간색 순서로 움직
        blue_pos = get_destination(blue_pos, move_dir)
        red_pos = get_destination(red_pos, move_dir)

# cnt번 기울였을 때
def find_min(cnt):
    global ans, red_pos, blue_pos
    
    # 파란색이 구멍으로 빠져 맵에 존재하지 않는다면 실패
    if not blue_exist():
        return
    
    # 파란색은 맵에 남아있지만 빨간색은 구멍으로 빠져 맵에 존재하지 않는다면
    # 성공이므로 답을 갱신하고 더 이상 탐색하지 않음
    if not red_exist():
        ans = min(ans, cnt)
        return
    
    # 이미 10번을 움직였는데도 성공하지 못했다면 탐색을 중단
    if cnt >= 10:
        return
    
    # 4 방향 중 한 방향을 정하여 움직
    for move_dir in range(4):
        # Tilt를 하면 blue, red 사탕의 위치가 바뀌게 되므로, 
		# tilt전 위치를 저장
        temp_red, temp_blue = red_pos, blue_pos
        
        # move_dir 방향으로 기울여 사탕의 위치를 변경
        tilt(move_dir)
        # 계속 탐색을 진행
        find_min(cnt + 1)
        
        # 탐색 후 퇴각하여 Tilt 전 상태로 복원하여 그 다음 방향으로도 동일한 기회줌
        red_pos, blue_pos = temp_red, temp_blue;

def char_to_int(elem):
    if elem == '.':
        return BLANK
    elif elem == '#':
        return BLOCK
    elif elem == 'R':
        return RED
    elif elem == 'B':
        return BLUE
    elif elem == 'O':
        return EXIT


a = [
    list(map(char_to_int, list(input())))
    for _ in range(N)
]

# 사탕의 경우 위치를 저장해두고, 맵에서는 지움
for i in range(N):
    for j in range(M):
        if a[i][j] == RED:
            a[i][j] = BLANK
            red_pos = (i, j)
        if a[i][j] == BLUE:
            a[i][j] = BLANK
            blue_pos = (i, j)

# backtracking을 이용해 최소 이동 횟수를 구함
find_min(0)

# 출력:

# 10번 이내로 답을 구할 수 없다면
# -1을 답으로 넣어줍니다.
if ans == 11:
    ans = -1

print(ans)

##################예제######################
"""
입력:
6 6
######
#.##B#
##R..#
#..#.#
#O...#
######

출력:
3
"""