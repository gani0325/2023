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

import copy

# move = [
#     [],
#     [(0, 1), (0, -1), (1, 0), (-1, 0)],
#     [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
#     [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]],
#     [[(0, 1), (0, -1), (-1, 0)], [(0, 1), (-1, 0), (1, 0)],
#      [(0, 1), (0, -1), (1, 0)], [(0, -1), (-1, 0), (1, 0)]],
#     [(0, 1), (0, -1), (1, 0), (-1, 0)]
# ]

# 세로, 가로
n, m = map(int, input().split())

# cctv 이동경로
move = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cctv = []
office = []
# 사무실 각 칸의 정보
for i in range(n):
    # [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 6, 0], [0, 0, 0, 0, 0, 0]]
    office.append(list(map(int, input().split())))
    for j in range(m):
        if office[i][j] in [1, 2, 3, 4, 5]:
            # cctv 종류, x, y 좌표
            # [[1, 2, 2]]
            cctv.append([office[i][j], i, j])

# 4방향에 빈칸 있는지
# office 정보, cctv 방향 정보(list 로 주어짐), cctv 위치


def check(graph, move, x, y):
    for i in move:
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]

            # 범위 벗어남
            if 0 > nx or 0 > ny or nx >= n or ny >= m:
                break
            # 벽
            if graph[nx][ny] == 6:
                break
            # 감시
            elif graph[nx][ny] == 0:
                # 걍 음수 만들어버려~~ 어차피 감시 못한 곳만 셀거임
                graph[nx][ny] -= -1

# cctv 개수 만큼 구현


def dfs(d, graph):
    global min_value

    # 계속 증가하며 확인했던 cctv를 끝까지 했을 때
    if d == len(cctv):
        cnt = 0
        for i in range(n):
            # 감시 못한 빈 공간 0 만 세기
            cnt += graph[i].count(0)
        min_value = min(min_value, cnt)
        return

    temp = copy.deepcopy(graph)
    # cctv 번호, cctv 위치
    cctv_num, x, y = cctv[d]

    for i in move[cctv_num]:
        check(temp, i, x, y)
        # 다음 cctv로 넘어가고, cctv 정보 갱신 & 끝났으면 return
        dfs(d + 1, temp)
        temp = copy.deepcopy(graph)


# 최댓값 해서 최소 수 만들기
min_value = int(1e9)
dfs(0, office)
print(min_value)
