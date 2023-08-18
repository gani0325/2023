"""
[23291] 어항 정리

💛 문제
마법사 상어는 그동안 배운 마법을 이용해 어항을 정리하려고 한다. 
어항은 정육면체 모양이고, 한 변의 길이는 모두 1이다. 
상어가 가지고 있는 어항은 N개이고, 가장 처음에 어항은 일렬로 바닥 위에 놓여져 있다. 
어항에는 물고기가 한 마리 이상 들어있다. 

<그림 1>은 어항 8개가 바닥 위에 놓여있는 상태이며, 
칸에 적힌 값은 그 어항에 들어있는 물고기의 수이다. 편의상 어항은 정사각형으로 표현했다.
=> 5, 2, 3, 14, 9, 2, 11, 8

어항을 한 번 정리하는 과정은 다음과 같이 이루어져 있다.

먼저, 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
만약, 그러한 어항이 여러개라면 물고기의 수가 최소인 어항 모두에 한 마리씩 넣는다. 
위의 예시의 경우 물고기의 수가 가장 적은 어항에는 물고기가 2마리 있고, 그러한 어항은 2개가 있다.
따라서, 2개의 어항에 물고기를 한 마리씩 넣어 <그림 2>와 같아진다.
=> 5, 3, 3, 14, 9, 3, 11, 8

이제 어항을 쌓는다. 먼저, 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항의 위에 올려 놓아 <그림 3>이 된다.
=> 5, 
=> 3, 3, 14, 9, 3, 11, 8

이제, 2개 이상 쌓여있는 어항을 모두 공중 부양시킨 다음, 전체를 시계방향으로 90도 회전시킨다. 
이후 공중 부양시킨 어항을 바닥에 있는 어항의 위에 올려놓는다. 
=> 3, 5, 
=> 3, 14, 9, 3, 11, 8
바닥의 가장 왼쪽에 있는 어항 위에 공중 부양시킨 어항 중 가장 왼쪽에 있는 어항이 있어야 한다. 
이 작업은 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 있을때까지 반복한다.
먼저, <그림 4>와 같이 어항이 놓인 상태가 변하고, 한 번 더 변해서 <그림 5>가 된다.
=> 3, 3, 
=> 14, 5, 
=> 9, 3, 11, 8

<그림 5>에서 한 번 더 어항을 공중 부양시키는 것은 불가능하다. 
그 이유는 <그림 6>과 같이 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 없기 때문이다.
=> 9, 14, 3
=> 3, 5, 3
=> 11, 8

공중 부양 작업이 모두 끝나면, 어항에 있는 물고기의 수를 조절한다.
모든 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다. 
이 차이를 5로 나눈 몫을 d라고 하자. d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다.
이 과정은 모든 인접한 칸에 대해서 동시에 발생한다. 이 과정이 완료되면 <그림 7>이 된다.
=> 5, 3
=> 10, 6
=> 9, 5, 10, 8

이제 다시 어항을 바닥에 일렬로 놓아야 한다. 가장 왼쪽에 있는 어항부터, 그리고 아래에 있는 어항부터 가장 위에 있는 어항까지 순서대로 바닥에 놓아야 한다. 
<그림 8>이 바닥에 다시 일렬로 놓은 상태이다.
=> 9, 10, 5, 5, 6, 3, 10, 8

다시 공중 부양 작업을 해야 한다. 이번에는 가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜 전체를 시계 방향으로 180도 회전 시킨 다음, 
오른쪽 N/2개의 위에 놓아야 한다. 이 작업은 두 번 반복해야한다. 
두 번 반복하면 바닥에 있는 어항의 수는 N/4개가 된다. 
<그림 9>는 이 작업을 1번 했을 때, <그림 10>은 다시 한 번 더 했을 때이다.

여기서 다시 위에서 한 물고기 조절 작업을 수행하고, 바닥에 일렬로 놓는 작업을 수행한다. <그림 10>에서 조절 작업을 마친 결과는 <그림 11>이 되고, 
여기서 다시 바닥에 일렬로 놓는 작업을 수행하면 <그림 12>가 된다.

어항의 수 N, 각 어항에 들어있는 물고기의 수가 주어진다. 
물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 어항을 몇 번 정리해야하는지 구해보자.

💚 입력
첫째 줄에 N, K가 주어진다. 
둘째에는 어항에 들어있는 물고기의 수가 가장 왼쪽에 있는 어항부터 순서대로 주어진다.

💙 출력
물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 
어항을 몇 번 정리해야하는지 출력한다.
"""

from collections import deque
import sys

# 어항의 수 N, 각 어항에 들어있는 물고기의 수 K
n, k = map(int, sys.stdin.readline().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = list()

# [deque([5, 2, 3, 14, 9, 2, 11, 8])]
board.append(deque(list(map(int, sys.stdin.readline().split()))))

# 물고기가 가장 적은 어항에 물고기 한 마리 넣기
def push_fish(graph) :
    min_bowl_fish_num = min(graph[0])

    for i in range(len(graph[0])):
        if graph[0][i] == min_bowl_fish_num:
            # 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다
            graph[0][i] += 1

# 가장 왼쪽의 어항을 위에 쌓기
def popleft_stack(graph) :
    pop = graph[0].popleft()
    graph.append(deque([pop]))

# 공중에 뜬 어항들 시계방향 90도 회전
def rotate_90_clock(bowls) :
    new_bowls = [[0] * len(bowls) for _ in range(len(bowls[0]))]

    for i in range(len(bowls[0])):
        for j in range(len(bowls)):
            new_bowls[i][j] = bowls[j][len(bowls[0])-1-i]

    return new_bowls
    
# 2개 이상 쌓인 어항들 분리해서 공중부양
def fly_bowls(graph) :
    while True :
        if len(graph) > len(graph[0]) - len(graph[-1]) :
            break

        will_fly = []
        will_fly_row = len(graph)
        will_fly_col = len(graph[-1])

        for i in range(will_fly_row) :
            new_deque = deque()

            for _ in range(will_fly_col) :
                new_deque.append(graph[i].popleft())

            will_fly.append(new_deque)

        graph = [graph[0]]

        rotated_bowls = rotate_90_clock(will_fly)
        for r in rotated_bowls :
            graph.append(deque(r))
    return graph

# 어항의 물고기 수 조절
def fix_fish_num (graph) :
    dp = [[0] * len(graph[x]) for x in range(len(graph))]

    for x in range(len(graph)) :
        for y in range(len(graph[x])) :
            for d in direction :
                nx = x + d[0]
                ny = y + d[1]
                # 모든 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다. 
                # 이 차이를 5로 나눈 몫을 d
                # d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다.
                # 이 과정은 모든 인접한 칸에 대해서 동시에 발생
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]) :
                    # 현재 칸이 더 크다면
                    if graph[x][y] > graph[nx][ny]:
                        d = (graph[x][y] - graph[nx][ny]) // 5
                        if d >= 1:
                            dp[x][y] -= d
                    else:
                        d = (graph[nx][ny] - graph[x][y]) // 5
                        if d >= 1:
                            dp[x][y] += d

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] += dp[i][j]


# 어항 일렬로 놓기
def bowl_row (graph) :
    new_graph = deque()

    for i in range(len(graph[-1])):
        for j in range(len(graph)):
            new_graph.append(graph[j][i])

    for i in range(len(graph[-1]), len(graph[0])):
        new_graph.append(graph[0][i])

    result_list = list()
    result_list.append(new_graph)

    return result_list

# 180도 회전
def rotate_180 (graph) :
    new_graph = []

    for i in reversed(range(len(graph))):
        graph[i].reverse()
        new_graph.append(graph[i])

    return new_graph


# 다시 공중부양 (절반 자르는데 2번 하기)
def fly_bowls2 (graph) :
    left1 = list()
    left2 = list()
    new_deque1 = deque()

    for i in range(n//2):
        new_deque1.append(graph[0].popleft())
    left1.append(new_deque1)

    rotated_left1 = rotate_180(left1)
    graph += rotated_left1

    for i in range(2):
        temp_deque = deque()
        for j in range(n//4):
            temp_deque.append(graph[i].popleft())
        left2.append(temp_deque)

    rotated_left2 = rotate_180(left2)
    graph += rotated_left2


# 물고기 가장 많은 어항과 가장 적은 어항의 차이
def get_result(graph):
    dq = graph[0]
    result1 = max(dq) - min(dq)
    
    return result1

answer = 0
while True :
    result = get_result(board)

    if result <= k :
        print(answer)
        break

    push_fish(board)
    popleft_stack(board)
    board = fly_bowls(board)

    fix_fish_num(board)
    board = bowl_row(board)

    fly_bowls2(board)
    fix_fish_num(board)
    board = bowl_row(board)
    answer += 1