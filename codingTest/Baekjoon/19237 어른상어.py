# 어른 상어
# 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다
# 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다
# 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데,
# 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다

# N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다
# 1) 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
# 2) 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다
# 3) 냄새는 상어가 k번 이동하고 나면 사라진다

# 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다
#     가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위
#     우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 다름
#     상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다
# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면,
#     가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다

# 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램
# 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력

# 첫 줄에는 N, M, k가 주어진다 (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)
# 그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습
#     0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미
# 그 다음 줄에는 각 상어의 방향
#     1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
# 그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다
#     첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위
#     두 번째 줄은 아래를 향할 때의 우선순위
#     세 번째 줄은 왼쪽을 향할 때의 우선순위
#     네 번째 줄은 오른쪽을 향할 때의 우선순위
#     각 우선순위에는 1부터 4까지의 자연수
#     가장 먼저 나오는 방향이 최우선
# 맨 처음에는 각 상어마다 인접한 빈 칸이 존재

import copy
# N×N 크기의 격자 중 M마리의 상어가 한 마리씩, k 초 동안 냄새 유지
n, m, k = map(int, input().split())
# 0은 빈칸이고, 0이 아닌 수 x는 x번 상어 (상어의 번호로 존재 표시)
sea = [list(map(int, input().split())) for _ in range(n)]
# 상어의 냄새표현 위해 냄새 타이머, 상어의 번호
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# 각 상어의 방향 (1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽)
s_dir = [0] + list(map(int, input().split()))
dir = [[]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 각 상어의 방향 우선순위
for i in range(m):
    array = []
    for j in range(4):
        array.append(list(map(int, input().split())))
    dir.append(array)


# 1) 상어 이동
def move(sea):
    global out
    s = copy.deepcopy(sea)
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 0:
                continue
            # 상어 번호
            s_n = s[i][j]
            # 상어 번호로 방향 확인
            d = s_dir[s_n]
            x, y = i, j
            what = False

            for p in range(4):
                nd = dir[s_n][d - 1][p]
                nx = x + dx[nd - 1]
                ny = y + dy[nd - 1]
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                # 냄새 타이머, 상어의 번호
                # 상어의 냄새가 존재하지 않을 때
                # 이동할 위치에 만약 상어가 존재하지 않다면 해당 위치로 상어를 이동
                if smell[nx][ny][1] == 0:
                    if s[nx][ny] == 0:
                        s[nx][ny] = sea[x][y]
                        s[x][y] = 0
                    # 해당 위치에 상어가 존재한다면 상어의 숫자를 비교해서 숫자가 더 크면
                    # 그 상어를 퇴출 시키고 퇴출 상어 수를 1 증가
                    else:
                        if s[nx][ny] > s[x][y]:
                            s[nx][ny] = sea[x][y]
                        out += 1
                        s[x][y] = 0
                    s_dir[s_n] = nd
                    what = True
                    break
            if what:
                continue

            # 4방향 다 모두 상어 냄새 난다면,
            # 상어의 냄새가 현재 상어 번호에 해당하는 냄새라면 그 곳으로 이동
            for p in range(4):
                nd = dir[s_n][d-1][p]
                nx = x + dx[nd - 1]
                ny = y + dy[nd - 1]
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if smell[nx][ny][1] == s_n:
                    s[nx][ny] = sea[x][y]
                    s[x][y] = 0
                    s_dir[s_n] = nd
                    break
    return s


# 2) 상어 냄새 타이머
# 현재 상어의 위치에 냄새를 뿌리고, move() 함수로 상어의 이동을 처리
def s_smell(k):
    for i in range(n):
        for j in range(n):
            if sea[i][j] != 0:
                # 냄새와 상어 번호
                smell[i][j][0], smell[i][j][1] = k, sea[i][j]


def smell_down():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] == 0:
                continue
            # 냄새 1에서 0으로 사라졋
            if smell[i][j][0] == 1:
                smell[i][j][0], smell[i][j][1] = 0, 0
            # 냄새 -1
            else:
                smell[i][j][0] -= 1

count = 0
out = 0
while True:
    if count >= 1000:
        count = -1
        break
    s_smell(k)
    sea = copy.deepcopy(move(sea))
    count += 1
    # 퇴출된 상어의 수가 (m-1)개, 즉 남은 상어 1마리면 끝~
    if out == m-1:
        break
    smell_down()

print(count)
