"""
[1036] 36진수

💛 문제
36진법의 숫자는 0부터 9까지의 수와 알파벳 A에서 Z로 나타낸다. 
A부터 Z까지 알파벳은 10부터 35에 차례대로 대응한다.

36진법의 수 N개가 주어진다. 36진법 숫자(0-9, A-Z) 중에서 K개의 숫자를 고른다. 
그러고 나서 N개의 수 모두에서 나타난 그 숫자를 Z로 바꾼다. 
그 이후에 N개의 수를 모두 더한다.

이때 가능한 합의 최댓값을 구하는 프로그램을 작성하시오. 
합의 최댓값도 36진수로 출력한다.

💚 입력
첫째 줄에 수의 개수 N이 주어진다. 
둘째 줄부터 N개의 줄에 수가 주어진다. N은 최대 50이고, 수의 길이도 최대 50이다. 
마지막 줄에 K가 주어진다. K는 36보다 작거나 같은 자연수 또는 0이다.

💙 출력
첫째 줄에 문제의 정답을 출력한다.
"""

# 수의 개수
N = int(input())
# 36진법 숫자(0-9, A-Z)
nums = [input() for _ in range(N)]
# K개의 숫자를 고른다
K = int(input())

num36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num36_diff = []
num_sum = 0
num_sep = []

# 현재값들의 합 구함
for i in nums:
    temp = []
    temp.extend(i)
    num_sep.append(temp)
    num_sum += int(i, 36)

# 각 문자를 Z로 변경했을 때 합의 변화량
for k in num36:
    sum_diff = 0

    for i in num_sep:
        temp = ''
        for n in i:
            if n == k:
                temp += 'Z'
            else:
                temp += n
        # 특정 문자를 변경했을 때 증가량(변경 후 합 - 변경 전 합
        sum_diff += int(temp, 36)
    num36_diff.append(sum_diff - num_sum)

# 최대값
maxmax = num_sum + sum(sorted(num36_diff, reverse=True)[:K])

# 36진수 변환
result = ''
while maxmax:
    result = num36[maxmax % 36] + result
    maxmax //= 36

if result :
    print(result)
else :
    print(0)