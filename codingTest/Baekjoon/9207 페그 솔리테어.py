"""
[9207] 페그 솔리테어

💛 문제
페그 솔리테어는 구멍이 뚫려있는 이차원 게임판에서 하는 게임이다. 각 구멍에는 핀을 하나 꽂을 수 있다.

핀은 수평, 수직 방향으로 인접한 핀을 뛰어넘어서 그 핀의 다음 칸으로 이동하는 것만 허용된다. 
인접한 핀의 다음 칸은 비어있어야 하고 그 인접한 핀은 제거된다.

현재 게임판에 꽂혀있는 핀의 상태가 주어진다.
이때, 핀을 적절히 움직여서 게임판에 남아있는 핀의 개수를 최소로 하려고 한다. 
또, 그렇게 남기기 위해 필요한 최소 이동횟수를 구하는 프로그램을 작성하시오.

💚 입력
첫째 줄에 테스트 케이스의 개수 1 ≤ N ≤ 100이 주어진다. 각 테스트 케이스는 게임판의 초기 상태이다.
게임판은 모두 같은 모양을 가진다. 
'.'는 빈 칸, 'o'는 핀이 꽂혀있는 칸, '#'는 구멍이 없는 칸이다. 핀의 개수는 최대 8이며, 
각 테스트 케이스는 빈 줄로 구분되어져 있다.

💙 출력
각 테스트 케이스에 대해서, 핀을 움직여서 남길 수 있는 핀의 최소 개수와 
그 개수를 만들기 위해 필요한 최소 이동 횟수를 출력한다.
"""

from sys import stdin # 입력이 많지는 않지만 그래도 해주는 것이 좋다.
input=stdin.readline

dx=[0,0,1,-1] 
dy=[1,-1,0,0]

def solve(cnt):
    global remains, moves
    array=[]
    for i in range(5):
        for j in range(9):
                        # 현재 위치에 페그가 있는지 확인
            if graph[i][j]=='o':
                array.append((j,i))
                
    if len(array) < remains:
        moves = cnt
        remains = len(array) 

    for x,y in array:
        for i in range(4): # 4방향 이동
            nx=x+dx[i]
            ny=y+dy[i]
            # 페그를 움직일 수 있는 조건 확인
            if -1<nx+dx[i]<9 and -1<ny+dy[i]<5:
                if graph[ny][nx]=='o' and graph[ny+dy[i]][nx+dx[i]]=='.':
                    graph[ny][nx]='.'
                    graph[ny+dy[i]][nx+dx[i]]='o'
                    graph[y][x]='.'
                    solve(cnt+1)
                    
                    # 을 제거 이전상태
                    graph[ny][nx]='o'
                    graph[ny+dy[i]][nx+dx[i]]='.'
                    graph[y][x]='o'
                    
# 테스트 케이스의 개수
n = int(input())

for _ in range(n):
    # '.'는 빈 칸, 'o'는 핀이 꽂혀있는 칸, '#'는 구멍이 없는 칸
    graph = [list(input().rstrip()) for i in range(5)]
    input()
    
    # 핀을 움직여서 남길 수 있는 핀의 최소 개수와 그 개수를 만들기 위해 필요한 최소 이동 횟수
    remains, moves = 10, 10
    solve(0)
    print(remains, moves)