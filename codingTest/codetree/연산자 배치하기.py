# codetree 참고함
# 연산자 배치하기
# n개의 정수가 순서대로 주어질 때, n−1개의 연산자를 정수 사이에 하나씩 배치
# 주어진 정수의 순서를 바꿀 수 없으며, 연산자는 덧셈, 뺄셈, 곰셈

# 연산자 간의 우선 순위를 무시하고 차례대로 연산 하였을 때, 가능한 식의 최솟값과 최댓값을 출력

# 첫 번째 줄에는 n
# 두 번째 줄에는 n개의 정수
# 세 번째 줄에는 사용 가능한 덧셈, 뺄셈, 곱셈의 개수

# 연산자의 인덱스가 i일 때 숫자는 i+1 번째 인덱스에 해당하는 값으로 계산

import sys

OPERATOR_NUM = 3
INT_MIN, INT_MAX = -sys.maxsize, sys.maxsize

# n개의 정수
n = int(input())
# n개의 정수
numbers = list(map(int, input().split()))
# 0: 덧셈, 1: 뺄셈, 2: 곱셈 (n-1개)
operator_cnt = list(map(int, input().split()))
operators = []

# 9223372036854775807, -9223372036854775807
min_val, max_val = INT_MAX, INT_MIN 

# 모든 연산자가 선택됐을 때 만들어진 식의 값을 반환
def calculate():
    # 가장 처음으로 입력 받은 숫자를 초기값
    val = numbers[0]
    
    # 연산자를 순서대로 적용하여 결과 값을 계산
    for i, operator in enumerate(operators):
        if operator == 0:
            # 연산자의 인덱스가 i일 때 숫자는 i+1 번째 인덱스에 해당하는 값으로 계산
            val += numbers[i + 1]
        elif operator == 1:
            val -= numbers[i + 1]
        else:
            val *= numbers[i + 1]
    
    return val

# 사용한 연산자가 주어진 연산자의 개수를 초과하는지 여부를 판별
def is_available():
    # all : 모두 True
    return all([cnt >= 0 for cnt in operator_cnt])

def find_min_and_max(cnt):
    global min_val, max_val
    
    # 모든 연산자가 선택됐을 때 만들 수 있는 값으로 정답을 갱신
    if cnt == n - 1:
        if is_available():
            val = calculate()
            min_val = min(min_val, val)
            max_val = max(max_val, val)
        return
    
    # 사용 가능한 연산자의 후보들을 탐색
    for i in range(OPERATOR_NUM):
        operators.append(i)
        operator_cnt[i] -= 1
        
        find_min_and_max(cnt + 1)
        
        operators.pop()
        operator_cnt[i] += 1

        
find_min_and_max(0)
print(min_val, max_val)

##################예제######################
"""
입력:
3
1 5 3
1 1 0

출력:
-1 3
"""