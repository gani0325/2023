# 낚시왕
# 낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판
# 칸에는 상어가 최대 한 마리 (상어는 크기와 속도를 가지고 있다)

# 낚시왕은 처음에 1번 열의 한 칸 왼쪽
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춤
# 1초 동안 일어나는 일
# 1. 낚시왕이 오른쪽으로 한 칸 이동
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡음
# 상어를 잡으면 격자판에서 잡은 상어가 사라짐
# 3. 상어가 이동
# 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초
# 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동

# 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있음
# 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹음

# 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합

# 첫째 줄에 격자판의 크기 R, C와 상어의 수 M
# 둘째 줄부터 M개의 줄에 상어의 정보
# (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
# d가 1 위, 2 아래, 3 오른쪽, 4 왼쪽
# 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없음

# 격자판의 크기 R, C와 상어의 수 M
r, c, m = map(int, input().split())
# 북 - 남 - 동 - 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
# 3차원 배열
graph = [[[] for _ in range(c)] for _ in range(r)]

for _ in range(m):
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
    x, y, s, d, z = map(int, input().split())
    # 상어의 정보 (크기, 속력, 이동방향)을 입력받아 저장
    graph[x - 1][y - 1].append([z, s, d - 1])


def moving():
    g = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j]:
                x, y = i, j
                # 상어의 정보 (크기, 속력, 이동방향)
                z, s, d = graph[i][j][0]
                s_count = s
                # 속력이 끝날 때 까지 반복
                while s_count > 0:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 경계선을 넘어간다면
                    if 0 > nx or nx >= r or ny < 0 or ny >= c:
                        # 북 -> 남, 남 -> 북, 동 -> 서, 서- > 동으로 방향을 변경
                        if d in [0, 2]:
                            d += 1
                        elif d in [1, 3]:
                            d -= 1
                        continue
                    else:
                        x, y = nx, ny
                        s_count -= 1
                # g에 저장된 상어의 위치와 정보
                g[x][y].append([z, s, d])
    # graph 리스트에 저장
    for i in range(r):
        for j in range(c):
            graph[i][j] = g[i][j]


eat_count = 0

for i in range(c):
    for j in range(r):
        if graph[j][i]:
            # 가장 가까운 상어
            value = graph[j][i][0]
            # 먹어라!
            eat_count += value[0]
            # 없어져라!
            graph[j][i].remove(value)
            break
    # 1초동안 움직여!
    moving()

    for p in range(r):
        for q in range(c):
            # 두 마리 이상이 같은 칸에 있을 경우
            if len(graph[p][q]) >= 2:
                # 먼저 정렬해봐! (큰 놈부터)
                graph[p][q].sort(reverse=True)
                # 큰 놈이 1마리 될 때까지
                while len(graph[p][q]) >= 2:
                    # 없어져랑! 먹어버려! (오른쪽 없어지지롱 작은 놈부터)
                    graph[p][q].pop()
print(eat_count)