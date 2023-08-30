"""
[1260] DFS와 BFS 

💛 문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

💚 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

💙 출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.
"""

from collections import deque

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 재귀 사용
def dfs(graph, v):
    print(v, end=' ')

    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)

# queue 사용
def bfs(graph, v) :
    queue = deque()
    queue.append(v)
    # 초기화
    visited = [False for _ in range(N + 1)]

    # 방문함
    visited[v] = True

    while queue :
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v] :
            # 관련된 노드에 방문 처리하기
            if not visited[i] :
                visited[i] = True
                # 방문한 노드도 살펴보기 위에 queue 에 넣기
                queue.append(i)


visited = [False for _ in range(N + 1)]

# 작은노드부터 우선 방문
for i in range(1, N+1):
    graph[i].sort()

# V부터 방문된 점을 순서대로 출력
dfs(graph, V)
print()
bfs(graph, V)