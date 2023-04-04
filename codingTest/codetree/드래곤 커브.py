# codetree 참고함
# 드래곤 커브
# 좌표평면은 x 값이 위에서 아래로 갈수록 증가 0에서부터 시작, y는 왼쪽에서 오른쪽으로 갈수록 증가 0에서부터 시작

# 0차 드래곤 커브는 길이가 1인 선분
# 1차 드래곤 커브는 0차 드래곤 커브를 복제한 후 커브의 끝점을 기준으로 시계방향으로 90도 회전하여 연결
# (끝점은 해당 드래곤 커브에서 시작점으로부터 가장 멀리 떨어진 점)
# n차 드래곤 커브는 n-1차 드래곤 커브의 끝점에 n-1차 드래곤 커브를 복제한 뒤 시계방향으로 90도 회전시킨 뒤 연결

# 크기 100×100의 좌표평면 위에 n개의 드래곤 커브가 주어질 때 만들어지는 단위 정사각형의 개수

# 첫번째 줄에는 드래곤 커브의 개수 n
# 두번째 줄부터 n + 1번째 줄까지는 드래곤 커브의 정보
# 드래곤 커브의 시작점 x, y, 시작 방향 d, 차수 g
# x는 위에서부터 아래로 가며 크기가 증가하고 0부터 시작
# y는 왼쪽에서부터 오른쪽으로 가며 크기가 증가하고 0부터 시작
# 방향은 0이상 3이하의 정수 (오른쪽, 위쪽, 왼쪽, 아래쪽)

GRID_SIZE = 100

# n개의 드래곤 커브
n = int(input())

# 현재 드래곤 커브를 이루고 있는 점들의 위치를 나타내는 배열
dragon_point = [[False for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]

# 현재 세대에서 새롭게 그려지는 드래곤 커브 점들을 나타내는 배열
new_dragon_point = [[False for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]

# 최종적으로 그려지는 드래곤 커브들의 점들을 나타내는 배열
paper = [[False for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]

# (x, y)점을 (center_x, center_y)를 기준으로 시계방향으로 90' 회전변환 했을 떄의 좌표값을 반환
def rotate(x, y, center_x, center_y):
    return (y - center_y + center_x, center_x - x + center_y)

# (center_x, center_y) 위치를 기준으로 dragon point 점들을 전부 시계 방향으로 90' 회전변환 시켜 해당 위치에 점을 추가
def simulate(center_x, center_y):
    # 새로운 dragon point 값을 초기화
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            new_dragon_point[i][j] = False
            
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            if dragon_point[i][j]:
                next_x, next_y = rotate(i, j, center_x, center_y)
                new_dragon_point[next_x][next_y] = True
    
    # 새로운 dragon point들을 현재 dragon point에 추가
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            if new_dragon_point[i][j]:
                dragon_point[i][j] = True

def draw_dragon_curve(x, y, d, g):
    # dragon_point 값을 초기화
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            dragon_point[i][j] = False
            
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
    
    # 0차 드래곤 커브
    start_x, start_y = x, y
    end_x, end_y = x + dxs[d], y + dys[d]
    
    dragon_point[start_x][start_y] = True
    dragon_point[end_x][end_y] = True
    
    # g번에 걸쳐 드래곤 커브를 확장
    for _ in range(g):
        # 드래곤 커브를 확장
        simulate(end_x, end_y)
        
        # 현재 드래곤 커브의 마지막 위치를 갱신
        end_x, end_y = rotate(start_x, start_y, end_x, end_y)
    
    # g차 드래곤 커브 점들을 paper에 전부 표시
    for i in range(GRID_SIZE + 1):
        for j in range(GRID_SIZE + 1):
            if dragon_point[i][j]:
                paper[i][j] = True

for _ in range(n):
    x, y, d, g = map(int, input().split())
    draw_dragon_curve(x, y, d, g)

# 4개의 꼭지점이 전부 드래곤 커브의 일부인 칸의 개수를 세기
ans = sum([
    1
    for i in range(GRID_SIZE)
    for j in range(GRID_SIZE)
    if paper[i][j] and paper[i][j + 1] 
    and paper[i + 1][j] and paper[i + 1][j + 1]
])

# 출력:
print(ans)

##################예제######################
"""
입력:
2
1 1 2 3
2 2 2 4

출력:
9
"""