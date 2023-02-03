# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
# 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수

# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다
# 주어진 항공권은 모두 사용
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 

def solution(tickets):
    tickets.sort(reverse = True)
    
    # 경로
    routes = dict()
    
    for start, end in tickets :
        # 출발정보가 이미 경로에 있다면
        if start in routes :
            routes[start].append(end)
        else :
            routes[start] = [end]
    
    st = ['ICN']
    answer = []

    while st :
        top = st[-1]
        
        # 해당 나라가 routes에 없거나, 0일 경우
        if top not in routes or len(routes[top]) == 0 :
            answer.append(st.pop())
        else :
            st.append(routes[top].pop())
    
    answer.reverse()
    return answer