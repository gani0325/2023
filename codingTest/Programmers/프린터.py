# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
# 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다

# 문서의 중요도가 순서대로 담긴 배열 priorities
# 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location

from collections import deque

def solution(priorities, location):
    que = deque([])
    
    for i in range(len(priorities)) :
        # 인덱스, 중요도
        que.append((i, priorities[i]))
        
    # 가장 높은 우선순위
    high = max(que, key = lambda x : x[1])[1]
    
    # 출력 순위
    cnt = 1
        
    while que :
        high = max(que, key = lambda x : x[1])[1]
        idx, now = que.popleft()

        # 우선순위 가장 높음
        if now == high :
            if idx == location :
                # location과 같다면
                return cnt
                # 아니라면 출력 순위 증가
            cnt += 1
        else :
            que.append((idx, now))