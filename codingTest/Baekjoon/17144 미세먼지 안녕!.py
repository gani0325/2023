"""
[17144] 미세먼지 안녕!

💛 문제
미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 
공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 
구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. 
(r, c)는 r행 c열을 의미한다

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 
공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.
1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    확산되는 양은 Ar,c/5이고 소수점은 버린다.
    (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
2. 공기청정기가 작동한다.
    공기청정기에서는 바람이 나온다.
    위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

공기청정기의 바람은 다음과 같은 방향으로 순환한다.
방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

💚 입력
첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다.
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. 
-1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

💙 출력
첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
"""

import sys
input = sys.stdin.readline

# r X c 격자판, T초
r, c, t = map(int, input().split())
arr = []

for i in range(r) :
    arr.append(list(map(int, input().split())))    

up = -1
down = -1

# 공기청정기 위치
for i in range(r) :
    # 공기청정기가 설치된 곳은 Ar,c가 -1
    if arr[i][0] == -1 :
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread() :
    # 사방으로 확산된다
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    # 미세먼지가 확산된 temp
    temp = [[0] * c for _ in range(r)]

    for i in range(r) :
        for j in range(c) :
            # 미세먼지가 있다면!
            if arr[i][j] != 0 and arr[i][j] != -1 :
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1 :
                        # 확산되는 양은 Ar,c/5이고 소수점은 버린다
                        temp[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 
                arr[i][j] -= tmp

    for i in range(r) :
        for j in range(c) :
            arr[i][j] += temp[i][j]

# 공기청정기 위쪽
def air_up() :
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0

    # 행, 1열
    x, y = up, 1

    while True :
        nx = x + dx[direct]
        ny = y + dy[direct]

        if x == up and y == 0 :
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c :
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래
def air_down() :
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0

    # 행, 1열
    x, y = down, 1
    while True :
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0 :
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c :
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

for _ in range(t) :
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r) :
    for j in range(c) :
        if arr[i][j] > 0 :
            answer += arr[i][j]

print(answer)

# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0
# 188