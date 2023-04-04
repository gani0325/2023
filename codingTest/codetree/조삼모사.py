# codetree 참고함
# 조삼모사
# n개의 일이 주어질 때 이를 아침과 저녁으로 n/2개씩 나누어 처리
# 일마다 특성이 다름 -> 같이할 때의 업무 강도를 나타내는 업무 간의 상성 P(i,j) 존재

# 아침의 하는 일의 업무 강도와 저녁에 하는 일의 업무 강도의 차이의 최솟값 구하기

# 첫째 줄에 일의 양 n
# 두번째줄부터 (n+1)번째 줄까지는 업무 간의 상성 P(i, j)

# 모든 조합을 만들어낸 뒤, 각각 조합에 대한 아침 저녁 차를 구해 최솟값 구하기

import sys
INT_MAX = sys.maxsize

# 일의 양 n
n = int(input())
# 업무 간의 상성 P(i, j)
p = [list(map(int, input().split())) for _ in range(n)]
evening = [False for _ in range(n)]

ans = INT_MAX

# 아침과 저녁 간의 힘듦의 차이
def calc():
    morning_sum = sum([
        p[i][j]  
        for i in range(n)
        for j in range(n)
        if not evening[i] and not evening[j]
    ])
    evening_sum = sum([
        p[i][j]  
        for i in range(n)
        for j in range(n)
        if evening[i] and evening[j]
    ])
    return abs(morning_sum - evening_sum)

def find_min(curr_idx, cnt):
    global ans
    
    # 정확히 아침 / 저녁으로 n / 2개씩 일이 나뉨
    if cnt == n // 2:
        # 선택된 조합에 대해 합의 차이를 계산 -> 최솟값 찾기
        ans = min(ans, calc())
        return
    
    # n / 2 개로 나뉘지 못한 경우라면 바로 퇴각
    if curr_idx == n:
        return

    # curr_idx 번째 업무를 아침에 하는 경우
    find_min(curr_idx + 1, cnt)
    
    # curr_idx 번째 업무를 저녁에 하는 경우
    evening[curr_idx] = True
    find_min(curr_idx + 1, cnt + 1)
    evening[curr_idx] = False

find_min(0, 0)

# 출력:
print(ans)

##################예제######################
"""
입력:
4
0 5 9 1
3 0 5 10
4 4 0 7
1 12 6 0

출력:
5
"""

