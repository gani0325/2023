"""
거리두기 확인하기

💛 문제
개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 
개발 직군 면접인 만큼 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.
    대기실은 5개이며, 각 대기실은 5x5 크기입니다.
    거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
    단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

예를 들어,
    위 그림처럼 자리 사이에 파티션이 존재한다면 맨해튼 거리가 2여도 거리두기를 지킨 것입니다.	
    위 그림처럼 파티션을 사이에 두고 앉은 경우도 거리두기를 지킨 것입니다.	
    위 그림처럼 자리 사이가 맨해튼 거리 2이고 사이에 빈 테이블이 있는 경우는 거리두기를 지키지 않은 것입니다.
    응시자가 앉아있는 자리(P)를 의미합니다.	
    빈 테이블(O)을 의미합니다.	
    파티션(X)을 의미합니다.

5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 
자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 
각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

🧡 제한 사항
places의 행 길이(대기실 개수) = 5
    places의 각 행은 하나의 대기실 구조를 나타냅니다.
places의 열 길이(대기실 세로 길이) = 5
places의 원소는 P,O,X로 이루어진 문자열입니다.
    places 원소의 길이(대기실 가로 길이) = 5
    P는 응시자가 앉아있는 자리를 의미합니다.
    O는 빈 테이블을 의미합니다.
    X는 파티션을 의미합니다.
입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.
return 값 형식
    1차원 정수 배열에 5개의 원소를 담아서 return 합니다.
    places에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.
    각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.

💚 입출력
places	                                                     result
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],              [1, 0, 1, 1, 1]
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	
"""

from collections import deque

# bfs(p, [i, j, 0])
# 대기실 가로 길이, [places 행, places 열, 거리]
def bfs(p, q):
    queue = deque([q])
    
    visited = [[False] * 5 for _ in range(5)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while queue:
        x, y, d = queue.popleft()
        # 응시자 자리
        visited[x][y] = True
        
        # 주변 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt = d + 1
            
            # 거리 실패 or 성공 유무만 가리면 됨
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                
                # 응시자가 앉아있는 자리
                if p[nx][ny] == 'P':
                    # 거리가 2 이하면 제한 거리 실패!
                    if cnt <= 2:
                        return False
                
                # 빈 테이블을 의미
                elif p[nx][ny] == 'O':
                    if cnt == 1:
                        queue.append([nx, ny, cnt])
    return True

# 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열
def solution(places):
    answer = []
    
    for p in places:
        flag = 1
        
        # 대기실은 5개이며, 각 대기실은 5x5 크기
        for i in range(5):
            for j in range(5):
                # 응시자가 앉아있는 자리
                if p[i][j] == 'P':
                    ok = bfs(p, [i, j, 0])
                    if ok == 0:
                        flag = 0
                        
        # 각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1
        # 한 명이라도 지키지 않고 있으면 0       
        answer.append(flag)
        
    return answer