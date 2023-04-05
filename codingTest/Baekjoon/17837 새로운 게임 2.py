# 새로운 게임 2
# 크기가 N×N인 체스판에서 진행되고, 사용하는 말의 개수는 K개
# 말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있음
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나

# 게임은 체스판 위에 말 K개를 놓고 시작
# 말은 1번부터 K번까지 번호 + 이동 방향 (위, 아래, 왼쪽, 오른쪽)
# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
# 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다름
# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료

# 1. 흰색인 경우에는 그 칸으로 이동
# 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓기
# A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동
# 2. 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꿈
# 3. 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동
# 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있음
# 체스판을 벗어나는 경우에는 파란색과 같은 경우

# 체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때, 게임이 종료되는 턴의 번호
# 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력

# 첫째 줄에 체스판의 크기 N, 말의 개수 K
# 둘째 줄부터 N개의 줄에 체스판의 정보
# 칸의 색 (0은 흰색, 1은 빨간색, 2는 파란색)
# 다음 K개의 줄에 말의 정보
# 행, 열의 번호, 이동 방향 (→, ←, ↑, ↓)
# 같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않음

# 체스판의 크기 N, 말의 개수 K
n, k = map(int, input().split())
# 칸의 색 (0은 흰색, 1은 빨간색, 2는 파란색)
board = [list(map(int, input().split())) for _ in range(n)]
# 현재 체스판에 행과 열에 놓여져 있는 말의 번호
chess = [[[] for _ in range(n)] for _ in range(n)]
# 이동 방향 (→, ←, ↑, ↓)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 말의 위치(x,y) 방향(d)
horse = []

for i in range(k):
    # 행, 열의 번호, 이동 방향
    x, y, d = map(int, input().split())
    horse.append([x - 1, y - 1, d - 1])
    chess[x - 1][y - 1].append(i)
cnt = 0


def change_dir(d):
    # 반대로 방향 바꾸기
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d


def solve(h_num):
    x, y, d = horse[h_num]
    nx = x + dx[d]
    ny = y + dy[d]
    # 체스판 안이고, 파란색이라면! 방향 바꿔야됨
    if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
        d = change_dir(d)
        horse[h_num][2] = d
        nx = x + dx[d]
        ny = y + dy[d]
        # 체스판 안이고, 또 파란색이라면! 멈춰라
        if 0 > nx or nx >= n or 0 > ny or ny >= n or board[nx][ny] == 2:
            return True
    horse_up = []
    for h_idx, h_n in enumerate(chess[x][y]):
        # 이동한 말이랑 원래 있는 말이랑 겹친다면 올라타!
        if h_n == h_num:
            horse_up.extend(chess[x][y][h_idx:])
            chess[x][y] = chess[x][y][:h_idx]
            break

    # 빨간 색이라면 말 업구 있는 모둠 묶어서 (?) 순서 거꾸로~
    if board[nx][ny] == 1:
        # lit = [[[1,2],[3,4]], [[5], [6,7]]]
        # => [[[5], [6, 7]], [[1, 2], [3, 4]]]
        horse_up = horse_up[-1::-1]
    # 순서 다시 바꿔줘용
    for h in horse_up:
        horse[h][0], horse[h][1] = nx, ny
        chess[nx][ny].append(h)

    # 말 4개 올라타면 종료
    if len(chess[nx][ny]) >= 4:
        return False
    return True


while True:
    what = False
    if cnt > 1000:
        print(-1)
        break
    for i in range(k):
        if solve(i) == False:
            what = True
            break
    cnt += 1
    if what:
        print(cnt)
        break
