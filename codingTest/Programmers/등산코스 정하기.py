"""
등산코스 정하기

💛 문제
XX산은 n개의 지점으로 이루어져 있습니다. 각 지점은 1부터 n까지 번호가 붙어있으며, 
출입구, 쉼터, 혹은 산봉우리입니다. 
각 지점은 양방향 통행이 가능한 등산로로 연결되어 있으며, 서로 다른 지점을 이동할 때 
이 등산로를 이용해야 합니다. 이때, 등산로별로 이동하는데 일정 시간이 소요됩니다.

등산코스는 방문할 지점 번호들을 순서대로 나열하여 표현할 수 있습니다.

예를 들어 1-2-3-2-1 으로 표현하는 등산코스는 1번지점에서 출발하여 2번, 3번, 2번, 1번 지점을 순서대로 방문한다는 뜻입니다.
등산코스를 따라 이동하는 중 쉼터 혹은 산봉우리를 방문할 때마다 휴식을 취할 수 있으며, 
휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity라고 부르기로 합니다.

당신은 XX산의 출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 
다시 원래의 출입구로 돌아오는 등산코스를 정하려고 합니다. 
다시 말해, 등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 합니다.
당신은 이러한 규칙을 지키면서 intensity가 최소가 되도록 등산코스를 정하려고 합니다.

XX산의 지점 수 n, 각 등산로의 정보를 담은 2차원 정수 배열 paths, 
출입구들의 번호가 담긴 정수 배열 gates, 산봉우리들의 번호가 담긴 정수 배열 summits가 매개변수로 주어집니다. 
이때, intensity가 최소가 되는 등산코스에 포함된 산봉우리 번호와 intensity의 최솟값을 차례대로 
정수 배열에 담아 return 하도록 solution 함수를 완성해주세요. 
intensity가 최소가 되는 등산코스가 여러 개라면 그중 산봉우리의 번호가 가장 낮은 등산코스를 선택합니다.

🧡 제한 사항
2 ≤ n ≤ 50,000
n - 1 ≤ paths의 길이 ≤ 200,000
paths의 원소는 [i, j, w] 형태입니다.
    i번 지점과 j번 지점을 연결하는 등산로가 있다는 뜻입니다.
    w는 두 지점 사이를 이동하는 데 걸리는 시간입니다.
    1 ≤ i < j ≤ n
    1 ≤ w ≤ 10,000,000
    서로 다른 두 지점을 직접 연결하는 등산로는 최대 1개입니다.
1 ≤ gates의 길이 ≤ n
    1 ≤ gates의 원소 ≤ n
    gates의 원소는 해당 지점이 출입구임을 나타냅니다.
1 ≤ summits의 길이 ≤ n
    1 ≤ summits의 원소 ≤ n
    summits의 원소는 해당 지점이 산봉우리임을 나타냅니다.
출입구이면서 동시에 산봉우리인 지점은 없습니다.
gates와 summits에 등장하지 않은 지점은 모두 쉼터입니다.
임의의 두 지점 사이에 이동 가능한 경로가 항상 존재합니다.
return 하는 배열은 [산봉우리의 번호, intensity의 최솟값] 순서여야 합니다.

💚 입출력
n	paths	                                                                                    gates	summits	    result
6	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]	[1, 3]	[5]	        [5, 3]
7	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]	                        [1]	[2, 3, 4]	    [3, 4]
7	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]	            [3, 7]	[1, 5]	    [5, 1]
5	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]	                    [1, 2]	[5]	        [5, 6]
"""

# XX산의 지점 수 n, 각 등산로의 정보를 담은 2차원 정수 배열 paths, 
# 출입구들의 번호가 담긴 정수 배열 gates, 산봉우리들의 번호가 담긴 정수 배열 summits
import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    
    # i번 지점과 j번 지점을 연결하는 등산로가 있다
    # w는 두 지점 사이를 이동하는 데 걸리는 시간
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    visited = [False] * (n + 1)
    
    for summit in summits:
        visited[summit] = True

    max_int = 1e9
    distance = [max_int] * (n + 1)
    
    temp = []
    # 출입구들의 번호가 담긴 정수 배열
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(temp, [0, gate])

    # 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensit
    # 등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함
    # intensity가 최소가 되도록 등산코스를 정하기
    
    while temp:
        d, i = heapq.heappop(temp)
        
        # 산봉우리면 continue
        if distance[i] < d or visited[i]:
            continue
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(temp, [dd, j])

    result = [-1, max_int]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
            
    # [산봉우리의 번호, intensity의 최솟값]
    return result