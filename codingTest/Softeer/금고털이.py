# 금, 은, 백금 등의 귀금속 덩어리
# 배낭은 W ㎏까지 담을 수 있음
# 귀금속은 톱으로 자르면 잘려진 부분의 무게만큼 가치를 가짐

# 각 금속의 무게와 무게당 가격이 주어졌을 때
# 배낭을 채울 수 있는 가장 값비싼 가격?

import sys

input = sys.stdin.readline

# 배낭 무게, 귀금속 종류
W, N = map(int, input().split())

table = []
for i in range(N):
    m, p = map(int, input().split())
    table.append((m, p))

# 가격 비싼 순서대로 -> [(70,2),(90,1)]
table.sort(key=lambda x: x[1], reverse=True)

answer = 0
# 금속의 무게 Mi와 무게당 가격
for m, p in table:
    if W > m:
        answer += m * p  # 보석 무게 * 가치
        W -= m
    else:
        answer += W * p  # 잘라낸 보석 무게 * 가치
        break
print(answer)
