# 마법사 상어와 복제
# 4 × 4 크기의 격자에서 연습
# (r, c)는 격자의 r행 c열
# 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (4, 4)

# 격자에는 물고기 M마리
# 물고기는 격자의 칸 하나에 들어가 있으며, 이동 방향을 가지고 있음
# 이동 방향은 8가지 방향(상하좌우, 대각선) 중 하나
# 마법사 상어와 상어는 격자의 한 칸에 들어가있음
# 둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있음

# 상어의 마법 연습 한 번
# 1) 상어가 모든 물고기에게 복제 마법을 시전
# 복제 마법은 시간이 조금 걸리기 때문에, 5) 에서 물고기가 복제되어 칸에 나타남
# 2) 모든 물고기가 한 칸 이동
#     상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없음
#     각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
#     이동할 수 있는 칸이 없으면 이동을 하지 않음
# 3) 상어가 연속해서 3칸 이동
#     상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동
#     이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법
#     이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남김
#     가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동
#     그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용
# 4) 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라짐
# 5) 1) 에서 사용한 복제 마법이 완료
#     모든 복제된 물고기는 1)에서의 위치와 방향을 그대로 갖게 됨

# 격자에 있는 물고기의 위치, 방향 정보와 상어의 위치, 연습 횟수 S
# S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수

# 첫째 줄에 물고기의 수 M, 상어가 마법을 연습한 횟수 S
# 둘째 줄부터 M개의 줄에는 물고기의 정보 fx, fy, d
#     (fx, fy)는 물고기의 위치를 의미하고, d는 방향
#     1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 마지막 줄에는 sx, sy가 주어지며, 상어가 (sx, sy)에 있음
# 격자 위에 있는 물고기의 수가 항상 1,000,000 이하인 입력만 주어짐


# 복제 -> 물고기 이동 -> 상어의 이동 -> 복제마법
# 1) 물고기 움직임
def move_fish(arr):
    ret = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while arr[x][y]:
                d = arr[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + delta[i][0], y + delta[i][1]
                    # 상어 존재 X, 범위 안넘음, 냄새 안남 X
                    if (
                            nx, ny
                    ) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[
                            nx][ny]:
                        ret[nx][ny].append(i)
                        break
                else:
                    ret[x][y].append(d)
    return ret


# 2) 상어 움직임
def move_shark(s):
    x, y = s
    q = []
    # 현재좌표, 방문좌표, 방향점수, 총갯수,
    q.append((x, y, set(), '', 0))
    for _ in range(3):
        for _ in range(len(q)):
            x, y, visited, dir_score, cnt = q.pop(0)
            for i in range(1, 5):
                nx, ny = x + s_delta[i][0], y + s_delta[i][1]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if (nx, ny) in visited:
                        q.append((nx, ny, visited, dir_score + str(i), cnt))
                    else:
                        q.append((nx, ny, visited | {(nx, ny)},
                                  dir_score + str(i), cnt + len(tmp[nx][ny])))
    q.sort(key=lambda x: (x[4], -int(x[3])))
    x, y, visited, dir_score, cnt = q[-1]
    for i, j in visited:
        if tmp[i][j]:
            tmp[i][j].clear()
            smell[i][j] = 3
    return (x, y)


m, s = map(int, input().split())
fishes = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
s_delta = [0, (-1, 0), (0, -1), (1, 0), (0, 1)]

matrix = [[[] for _ in range(4)] for _ in range(4)]
for x, y, d in fishes:
    matrix[x][y].append(d)

shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0] * 4 for _ in range(4)]

for _ in range(s):
    # 물고기 복제
    tmp = [[k[:] for k in row] for row in matrix]
    # 물고기 한칸 이동
    # 이동 할 때까지 delta -1
    # 물고기 냄새 있거나 상어 있거나, 격자 판 넘어가면 이동 불가
    tmp = move_fish(tmp)
    # 상어 연속 3칸 이동
    # 상하좌우 인접한 칸 이동 가능
    # 범위 벗어나면 불가능
    shark = move_shark(shark)
    # 이동 중 물고기 있는 곳으로 가면 물고기 없어짐 -> 냄새 남김
    # 많이 먹을 수 있는 방법으로 감
    # 위 1, 좌 2, 아래 3, 오른 4 순으로 이동
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 물고기 배열 tmp fishes 에 더해줌
    for i in range(4):
        for j in range(4):
            matrix[i][j] += tmp[i][j]
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(matrix[i][j])

print(answer)
