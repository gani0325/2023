from collections import deque

# n개의 원판, 원판에는 M개의 정수, t번 회전
n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 동, 서, 남, 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def rotate(x, d, k) :
    queue = deque()
    queue.extend(graph[x])
    # 0인 경우는 시계 방향, 1인 경우는 반시계 방향
    if d == 0 :
        # 시계방향으로 k배 만큼 돌리기
        queue.rotate(k)
    else :
        # 반시계방향으로 k배 만큼 돌리기
        queue.rotate(-k)
    graph[x] = list(queue)

def change_arg() :
    arg_cnt = 0
    all_sum = 0
    for i in range(n) :
        for j in range(m) :
            # 처음 모든 제거된 숫자(0)을 제외한 나머지 숫자의 갯수와 
            # 그 숫자들의 합을 계산한 후,
            # 만약 모든 숫자가 0이라면 평균을 계산하지 않게 리턴
            if graph[i][j] != 0 :
                arg_cnt += 1
                all_sum += graph[i][j]
            
    if arg_cnt == 0:
        return False
    # 평균을 계산했다면 모든 원판에 들어있는 숫자들에 값과 비교
    avg = all_sum / arg_cnt
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] != 0 :
                # 평균 값보다 크다면 -1, 평균값보다 작다면 +1
                if graph[i][j] > avg :
                    graph[i][j] -= 1
                elif graph[i][j] < avg :
                    graph[i][j] += 1
    return True

# 인접한 곳에 숫자가 같은지 파악해서 만약 숫자가 같다면 원판에 숫자를 제거(0으로 변경)
# i번째 원판에는 즉, 0번 열과 m-1 열은 이어져 있으므로 인접 4방향을 살필 때, 값을 잘 변경해줘서 모든 원판에 인접한 곳을 방문
def solve(x, y) :
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    value = graph[x][y]
    graph[x][y] = 0
    cnt = 0
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > ny or ny >= m :
                if y == 0 :
                    ny = m -1
                elif y == m - 1:
                    ny = 0
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] :
                    if graph[nx][ny] == value :
                        cnt += 1
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        queue.append((nx, ny))
    if cnt == 0 :
        graph[x][y] = value
    return cnt

for _ in range(t) :
    # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전
    x, d, k = map(int, input().split())
    check_sum = 0
    for i in range(n) :
        check_sum += sum(graph[i])
        if (i+1) % x == 0 :
            rotate(i, d, k)
    if check_sum == 0 :
        break
    else :
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for i in range(n) :
            for j in range(m) :
                if not visited[i][j] and graph[i][j] != 0 :
                    cnt += solve(i, j)
        if cnt == 0 :
            change_arg()
answer = 0
for i in range(n) :
    answer += sum(graph[i])
print(answer)