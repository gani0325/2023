# 마법사 상어와 블리자드
# 크기가 N×N인 격자에서 연습
# N은 항상 홀수이고, (r, c)는 격자의 r행 c열
# 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)
# 마법사 상어는 ((N+1)/2, (N+1)/2)
# 일부 칸과 칸 사이에는 벽이 세워져 있으며, 실선은 벽, 점선은 벽이 아님
# 칸에 적혀있는 수는 칸의 번호
# 가장 처음에 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있음

# 구슬은 1번 구슬, 2번 구슬, 3번 구슬
#     같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면, 그 구슬을 연속하는 구슬
# 방향 di와 거리 si
#     4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4
# 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴
# 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸
# 얼음 파편은 벽의 위로 떨어지기 때문에, 벽은 파괴되지 않음

# 1) 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동 (걍 뒤에 있는 구슬이 쭈르륵 빈칸 채우는)
# 이 이동은 더 이상 구슬이 이동하지 않을 때까지 반복

# 2) 구슬이 폭발하는 단계
# 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생
# 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동
# 구슬이 이동한 후에는 다시 구슬이 폭발하는 단계이고, 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복

# 3) 구슬이 변화하는 단계
# 연속하는 구슬은 하나의 그룹
# 1번 구슬은 빨간색, 2번 구슬은 파란색, 3번 구슬은 보라색

# 하나의 그룹은 두 개의 구슬 A와 B로 변함
#     구슬 A의 번호는 그룹에 들어있는 구슬의 개수
#     B는 그룹을 이루고 있는 구슬의 번호
# 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어감
# 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라짐

# 마법사 상어는 블리자드를 총 M번 시전
# 시전한 마법의 정보가 주어졌을 때,
# 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)

# 첫째 줄에 N, M
# 둘째 줄부터 N개의 줄에는 격자에 들어있는 구슬의 정보
#     r번째 행의 c번째 정수는 (r, c)에 들어있는 구슬의 번호
#     어떤 칸에 구슬이 없으면 0이 주어짐
#     상어가 있는 칸도 항상 0이 주어짐
# 다음 M개의 줄에는 블리자드 마법의 방향 di와 거리 si

from collections import deque


# 토네이도 좌표 넣어주기
def indexing():
    cx, cy = n // 2, n // 2
    move = 0
    # 토네이도처럼 왼, 아래, 오른, 위
    nx = [0, 1, 0, -1]
    ny = [-1, 0, 1, 0]

    while True:
        # 상어가 있는 위치 (n/2, n/2)부터 좌->하->우->상을 반복
        # 1, 1, 2, 2, 3, 3, ..., n-1, n-1, n
        for i in range(4):
            if i % 2 == 0:
                move += 1
            for _ in range(move):
                cx += nx[i]
                cy += ny[i]
                graphIdx.append((cx, cy))
                if cx == 0 and cy == 0:
                    return


# 1) 매직~ 시전
def magic(dir, dist):
    x, y = n // 2, n // 2
    # 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(dist):
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        # 파편 맞았으니 다 없어져라!
        board[x][y] = 0
    # 채워!
    fill_blank()
    # 4개 연속이면 폭발!
    while bomb():
        # 다시 채워!
        fill_blank()
    # 그룹으로 묶어!
    grouping()


# 2) 빈칸 채워채워
def fill_blank():
    blankIdx = deque()
    for x, y in graphIdx:
        # 0인 칸을 발견하면 그 칸을 blankIdx라는 큐에 넣어준 상태
        if board[x][y] == 0:
            blankIdx.append((x, y))
        # 빈 칸을 만나지 않았을 때, 큐에서 빈칸의 인덱스를 꺼내어
        elif board[x][y] > 0 and blankIdx:
            nx, ny = blankIdx.popleft()
            # 그 칸에 현재 칸의 수를 넣어주고
            board[nx][ny] = board[x][y]
            # 현재 칸은 0으로 만들어줌으로써 당겨주기
            board[x][y] = 0
            # 모두 당겨질 때 까지 반
            blankIdx.append((x, y))


# 3) 연속된 숫자가 4칸 이상 존재한다면 그 칸들을 폭발
def bomb():
    visited = deque()
    cnt = 0
    num = -1
    flag = False
    for x, y in graphIdx:
        # 전 칸과 같은 숫자가 발생한다면 카운트를 늘려나감
        if num == board[x][y]:
            visited.append((x, y))
            cnt += 1
        else:
            # 점수계산을 해야 하므로 점수도 함께 저장
            if cnt >= 4:
                score[num - 1] += cnt
                flag = True

            while visited:
                nx, ny = visited.popleft()
                # 저장하고 있는 수의 카운트가 4 이상이라면 폭발
                # 그 칸들을 모두 0으로 바꿈
                if cnt >= 4:
                    board[nx][ny] = 0

            num = board[x][y]
            cnt = 1
            visited.append((x, y))

    return flag


def grouping():
    cnt = 1
    tmpx, tmpy = graphIdx[0]
    num = board[tmpx][tmpy]
    nums = []

    for i in range(1, len(graphIdx)):
        x, y = graphIdx[i][0], graphIdx[i][1]
        if num == board[x][y]:
            cnt += 1
        else:
            nums.append(cnt)
            nums.append(num)
            num = board[x][y]
            cnt = 1

    idx = 0
    for x, y in graphIdx:
        if not nums:
            break
        board[x][y] = nums[idx]
        idx += 1
        if idx == len(nums):
            break


# N X N 격자, 마법사 상어는 블리자드를 총 M번 시전
n, m = map(int, input().split())
# N개의 줄에는 격자에 들어있는 구슬의 정보
board = [list(map(int, input().split())) for _ in range(n)]
cmd = []
answer = 0
score = [0] * 3
graphIdx = deque()

for i in range(m):
    # 블리자드 마법의 방향 di와 거리 si
    d, s = map(int, input().split())
    cmd.append((d, s))

indexing()

for a, b in cmd:
    magic(a - 1, b)

for i in range(3):
    answer += (i + 1) * score[i]

print(answer)
