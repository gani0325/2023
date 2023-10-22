"""
[15683] 감시

💛 문제
스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다.
사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다

각 CCTV가 감시할 수 있는 방법은 다음과 같다.
    1번 CCTV는 한 쪽 방향만 감시할 수 있다.
    2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고,
    3번은 직각 방향이어야 한다.
    4번은 세 방향,
    5번은 네 방향을 감시할 수 있다.

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다.
사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다.
CCTV가 감시할 수 없는 영역은 사각지대라고 한다.

CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며,
감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다.

사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서,
사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.

💚 입력
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다.
CCTV의 최대 개수는 8개를 넘지 않는다.

💙 출력
첫째 줄에 사각 지대의 최소 크기를 출력한다.
"""

import queue

# 사무실 n * m
n, m = map(int, input().split())

# 사무실 각 칸의 정보
office = []
for _ in range(n):
    # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 6, 0], [0, 0, 0, 0, 0, 0]]
    office.append(list(map(int, input().split())))
# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
cctv = [[0] * m for _ in range(n)]
print(cctv)
dir1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir2 = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
dir3 = [[(0, 1), (-1, 0)], [(0, 1), (1, 0)],
        [(0, -1), (1, 0)], [(0, -1), (-1, 0)]]
dir4 = [[(0, 1), (0, -1), (-1, 0)], [(0, 1), (-1, 0), (1, 0)],
        [(0, 1), (0, -1), (1, 0)], [(0, -1), (-1, 0), (1, 0)]]
dir5 = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_range(nx, ny):
    # 범위 밖이면 0 return
    return 0 >= nx or nx > n or 0 >= ny or ny > m


def cnt_cctv(cctv):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cctv[i][j] == "#":
                cnt += 1
    return cnt


temp = []

max_cnt = 0
for i in range(n):
    for j in range(m):
        cnt = 0
        queue = queue()
        # cctv 종류 1 ~ 6
        if office[i][j] == 1:
            for k in range(len(dir1)):
                x = i + dir1[k][0]
                y = j + dir1[k][1]
                queue.append((x, y))

                while (queue):
                    nx, ny = queue.pop()
                    if (in_range(nx, ny) == 0):
                        break
                    # 빈 공간이거나 이미 감시 영역인 경우
                    if office[nx][ny] == 0 or office[nx][ny] == "#":
                        cctv[nx][ny] = "#"

                        # 한칸 더 전진
                        nx = nx + dir1[k][0]
                        ny = ny + dir1[k][1]
                        queue.append((nx, ny))
            max_cnt = max(cnt, cnt_cctv(cctv))

        if office[i][j] == 2:
            for k in range(len(dir1)):
                for p in range(len(dir1[k])):
                    x = i + dir2[k][p][0]
                    y = j + dir2[k][p][1]
                    queue.append((x, y))

                    while (queue):
                        nx, ny = queue.pop()
                        if (in_range(nx, ny) == 0):
                            break
                        # 빈 공간이거나 이미 감시 영역인 경우
                        if office[nx][ny] == 0 or office[nx][ny] == "#":
                            cctv[nx][ny] = "#"

                            # 한칸 더 전진
                            x = i + dir2[k][p][0]
                            y = j + dir2[k][p][1]
                            queue.append((nx, ny))

        if office[i][j] == 3:
            for k in range(len(dir1)):
                for p in range(len(dir1[k])):
                    x = i + dir3[k][p][0]
                    y = j + dir3[k][p][1]
                    queue.append((x, y))

                    while (queue):
                        nx, ny = queue.pop()
                        if (in_range(nx, ny) == 0):
                            break
                        # 빈 공간이거나 이미 감시 영역인 경우
                        if office[nx][ny] == 0 or office[nx][ny] == "#":
                            cctv[nx][ny] = "#"

                            # 한칸 더 전진
                            x = i + dir3[k][p][0]
                            y = j + dir3[k][p][1]
                            queue.append((nx, ny))

        if office[i][j] == 4:
            for k in range(len(dir1)):
                for p in range(len(dir1[k])):
                    x = i + dir4[k][p][0]
                    y = j + dir4[k][p][1]
                    queue.append((x, y))

                    while (queue):
                        nx, ny = queue.pop()
                        if (in_range(nx, ny) == 0):
                            break
                        # 빈 공간이거나 이미 감시 영역인 경우
                        if office[nx][ny] == 0 or office[nx][ny] == "#":
                            cctv[nx][ny] = "#"

                            # 한칸 더 전진
                            x = i + dir4[k][p][0]
                            y = j + dir4[k][p][1]
                            queue.append((nx, ny))
