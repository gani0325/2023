# 각 사람마다 “나보다 점수가 큰 사람”의 수를 세어 1을 더한 것이 자신의 등수가 된다
# 대회별 등수는 각 대회에서 얻은 점수를 기준으로 하며 최종 등수는 세 대회의 점수의 합을 기준
# 각 참가자의 대회별 등수 및 최종 등수를 출력하는 프로그램

import sys

input = sys.stdin.readline

N = int(input())

table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# 전체 등수
total_score = [0] * N
for i in range(len(table)):
    result = []

    for j in range(N):
        rank = 1
        total_score[j] += table[i][j]
        for k in range(N):
            if table[i][j] < table[i][k]:
                rank += 1
        result.append(rank)  # 각 대회의 등수
    print(*result)

total_rank = []
for i in range(N):
    rank = 1
    for j in range(N):
        if total_score[i] < total_score[j]:
            rank += 1
    total_rank.append(rank)

print(*total_rank)
