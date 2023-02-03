# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수

# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현

def solution(n, computers):
    def dfs(v) :
        # 방문함
        visited[v] = True
        
        for net in range(n) :
            # 방문 안했고 + 인접할 때
            if not visited[net] and computers[v][net] :
                dfs(net)
    cnt = 0
    visited = [False] * n
    
    for idx in range(n) :
        if not visited[idx] :
            dfs(idx)
            cnt += 1
    
    return cnt