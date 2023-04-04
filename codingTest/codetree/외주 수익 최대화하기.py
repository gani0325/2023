# codetree 참고함
# 외주 수익 최대화하기
# n일의 휴가 동안 외주 개발을 하여 수익을 최대화 
# 수행할 수 있는 외주 작업이 하루에 한 개씩, 각 외주 작업은 수행 완료하는데 걸리는 기한 t와 이를 완료 했을 때의 수익 p
# 두 개 이상의 외주 작업은 동시에 수행할 수 없으며, 휴가 기간 이후로는 일을 할 수 없다고 할 때 외주 수익의 최대값을 출력

# 첫 번째 줄에는 n이 주어지고,
# 두 번째 줄부터 n+1번째 줄까지는 각 일자에 수행할 수 있는 외주 작업의 기한 t와 수익 p

# n일의 휴가
n = int(input())

# 외주 작업의 기한 t와 수익 p
develop = [list(map(int, input().split())) for _ in range(n)]
times = [i[0] for i in develop]
profits = [i[1] for i in develop]

dp = profits[:]

for i in range(n):
    if times[i] + i > n:
        dp[i] = 0 # i지점에서 불가능한 경우(휴가가 끝나버리는 경우) 
    for j in range(i):
        if times[j] <= i - j:
            if times[i] + i <= n:
                # print(dp[i])
                # print(dp[j])
                # print(profits[i])
                dp[i] = max(dp[i], dp[j] + profits[i])
print(max(dp))

##################예제######################
"""
입력:
3
2 5
2 7
1 3

출력:
8
"""