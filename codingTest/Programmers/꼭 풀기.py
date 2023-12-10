# https://davinci-ai.tistory.com/34

# https://davinci-ai.tistory.com/35

N = int(input())
graph = [[0]*N for _ in range(N)]

#  서,남,동,북
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def tonade():
    time = 0
    sy,sx = N//2,N//2 # 중심에서 시작함
    graph[sy][sx] = 0
    for i in range(2*N - 1):
        d=i%4
        if d==0 or d==2:
            time+=1
            
        for _ in range(time):
            ny = sy+dy[d]
            nx = sx+dx[d]
            if 0<=ny<N and 0<=nx<N:
                graph[ny][nx] = graph[sy][sx]+1
                sy,sx = ny,nx

print(graph)            
tonade()

n = 5

list = [[0] * n for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        list[i][j] = cnt
        cnt += 1

print(list)
def gravity(graph): # 중력 작용해요~
    for col in range(N):
        for row in range(N-1,-1,-1):
            if graph[col][row] >= 0:
                for k in range(col+1,N+1):
                    if k == N or graph[k][row] >= -1:
                        graph[col][row], graph[k-1][row] = graph[k-1][row], graph[col][row]
                        return graph
print(gravity(list))