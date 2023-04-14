# 게임 맵 최단거리
# ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임
# 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리
# 검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길
# 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없음

# 게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 
# 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수
# 상대 팀 진영에 도착할 수 없을 때는 -1을 return

# n x m 크기의 게임 맵의 상태
# 0은 벽이 있는 자리, 1은 벽이 없는 자리
from collections import deque

def solution(maps):
    queue = deque()
    n = len(maps)
    m = len(maps[0])
    
    # 캐릭터는 게임 맵의 좌측 상단인 (1, 1)
    # 상대방 진영은 게임 맵의 우측 하단인 (n, m) 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue.append((0, 0))
    answer = 0
    
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    if maps[n-1][m-1] == 1 :
        answer = -1
    else :
        answer = maps[n-1][m-1]
    
    return answer