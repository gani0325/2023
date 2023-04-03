# codetree 참고함
# 바이러스 검사
# n개의 식당에 있는 고객들의 체온을 측정
# 체온을 측정하는 검사자는 검사팀장과 검사팀원 (한 가게당 팀장은 오직 한 명, 팀원은 여러명)
# 가게당 팀장 한 명은 무조건 필요! 가게에 검사팀원만 존재하는 경우는 X! 팀장이든 팀원이든 담당한 가게에 대해서만 검사

# n개의 식당 고객들의 체온을 측정하기 위해 필요한 검사자 수의 최솟값을 구하는 프로그램
# 첫째 줄에는 식당의 수 n
# 둘째 줄에는 각 식당에 있는 고객의 수
# 셋째줄에는 검사팀장이 검사할 수 있는 최대 고객 수와 검사팀원이 검사할 수 있는 최대 고객 수

n = int(input())
customers = list(map(int, input().split()))
leader, member = tuple(map(int, input().split()))

def required_member_num(customer_num):
    # 남은 고객이 없다면 검사 팀원은 필요가 없음
    if customer_num <= 0:
        return 0
    
    # 정확히 나누어 떨어지는 경우라면, 몫 만큼의 인원이 필요함
    if customer_num % member == 0:
        return customer_num // member
    # 나누어 떨어지지 않는 경우라면 1명이 추가적으로 더 필요함
    else:
        return (customer_num // member) + 1

ans = 0

# 식당별로 필요한 최소 검사자 수를 검색
for customer_num in customers:
    # 팀장은 꼭 한 명 필요
    ans += 1
    
    # 필요한 팀원 인원수만큼 더함
    ans += required_member_num(customer_num - leader)

# 출력
print(ans)

##################예제######################
"""
입력:
3
10 15 13
7 14

출력:
6
"""