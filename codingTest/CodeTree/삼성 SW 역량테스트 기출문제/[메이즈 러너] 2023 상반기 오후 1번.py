"""
💛 메이즈 러너
M명의 참가자가 미로 탈출하기 게임에 참가하였습니다.
미로의 구성은 다음과 같습니다.

    1. 미로는 N×N 크기의 격자입니다. 
        각 위치는 (r,c)의 형태로 표현되며, 아래로 갈수록 r이 증가, 오른쪽으로 갈수록 c가 증가합니다.
        좌상단은 (1,1)입니다.

    2. 미로의 각 칸은 다음 3가지 중 하나의 상태를 갖습니다.
        빈 칸
            참가자가 이동 가능한 칸입니다.
        벽
            참가자가 이동할 수 없는 칸입니다.
            1이상 9이하의 내구도를 갖고 있습니다.
            회전할 때, 내구도가 1씩 깎입니다.
            내구도가 0이 되면, 빈 칸으로 변경됩니다.
        출구
            참가자가 해당 칸에 도달하면, 즉시 탈출합니다.

1초마다 모든 참가자는 한 칸씩 움직입니다. 움직이는 조건은 다음과 같습니다.
    두 위치 (x1,y1), (x2,y2)의 최단거리는 ∣x1−x2∣+∣y1−y2∣로 정의됩니다.
    모든 참가자는 동시에 움직입니다.
    상하좌우로 움직일 수 있으며, 벽이 없는 곳으로 이동할 수 있습니다.
    움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
    움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
    참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다.
    한 칸에 2명 이상의 모험가가 있을 수 있습니다.

모든 참가자가 이동을 끝냈으면, 다음 조건에 의해 미로가 회전합니다.
    한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
    가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r 좌표가 작은 것이 우선되고, 
        그래도 같으면 c 좌표가 작은 것이 우선됩니다.
    선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎입니다.

K초 동안 위의 과정을 계속 반복됩니다. 만약 K초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝납니다. 
게임이 끝났을 때, 모든 참가자들의 이동 거리 합과 출구 좌표를 출력하는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 N, M, K가 공백을 사이에 두고 주어집니다.
다음 N개의 줄에 걸쳐서 N×N 크기의 미로에 대한 정보가 주어집니다.
    0이라면, 빈 칸을 의미합니다.
    1이상 9이하의 값을 갖는다면, 벽을 의미하며, 해당 값은 내구도를 뜻합니다.
다음 M개의 줄에 걸쳐서 참가자의 좌표가 주어집니다. 모든 참가자는 초기에 빈 칸에만 존재합니다.
다음 줄에 출구의 좌표가 주어집니다. 출구는 빈 칸에만 주어집니다.
    N: 미로의 크기 (4≤N≤10)
    M: 참가자 수 (1≤M≤10)
    K: 게임 시간 (1≤K≤100)

💚 출력 형식
게임 시작 후 K초가 지났거나, 모든 참가자가 미로를 탈출했을 때, 
모든 참가자들의 이동 거리 합과 출구 좌표를 출력합니다.

🐧 입출력 예제
예제1
➡️ 입력:
5 3 8
0 0 0 0 1
9 2 2 0 0
0 1 0 1 0
0 0 0 1 0
0 0 0 0 0
1 3
3 1
3 5
3 3

➡️ 출력:
7
1 1
"""

# 미로, 참가자, 게임시간
n, m, k = tuple(map(int, input().split()))
maze = [[] * n for _ in range(n)]

# 미로 N X N
for i in range(n):
    maze[i] = list(map(int, input().split()))
    # [[0, 0, 0, 0, 1], [9, 2, 2, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]

# 참가자 좌표 (-1, -2 ... 로 지정)
runner = []
for i in range(1, m+1):
    x, y = map(int, input().split())
    # 참가자 좌표 list
    runner.append((x, y))       # [(1, 3), (3, 1), (3, 5)]
    # 인덱스가 1부터 시작해서 -1 해준다
    # maze[x - 1][y - 1] = -i

# 출구 좌표
x, y = map(int, input().split())
runner.insert(0, (x, y))
# 인덱스가 1부터 시작해서 -1 해준다
maze[x - 1][y - 1] = 'X'

"""
[[0, 0, -1, 0, 1], 
[9, 2, 2, 0, 0], 
[-2, 1, 'X', 1, -3], 
[0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0]]
"""

# 참가자 이동 =>  출구 + 참가자 [(3, 3), (1, 3), (3, 1), (3, 5)]
# 출구와 가깝고, 상하 우선!
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
# 회전해야 하는 최소 정사각형을 찾아 기록해줍니다.
sx, sy, square_size = 0, 0, 0
# 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의해줍니다.
next_maze = [
    [0] * (n + 1)
    for _ in range(n + 1)
]


def move():
    global runner, ans

    # 출구의 좌표
    x, y = runner[0]
    x -= 1
    y -= 1
    for i in range(1, m+1):
        r, c = runner[i]
        r -= 1
        c -= 1

        for j in range(4):
            nx = r + dx[j]
            ny = c + dy[j]
            if (0 <= nx < n and 0 <= ny < n):
                # 빈칸이거나 참가자 자리라면
                if (maze[nx][ny] == 0):
                    # 처음 출구와의 거리보다 멀어지면
                    if (abs(r - x) < abs(r - nx)) or (abs(c - y) < abs(c - ny)):
                        continue
                    else:
                        # |x1 - x2] + |y1 - y2|
                        # 이동한다
                        runner[i] = nx, ny
                        # maze[nx][ny] = i
                        maze[r][c] = 0
                else:
                    continue
    return runner, maze
