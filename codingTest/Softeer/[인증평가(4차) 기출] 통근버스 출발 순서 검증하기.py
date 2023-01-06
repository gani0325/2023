# 임시 주차장은 출입구가 하나밖에 없는 데다가,
# 폭이 좁아서 스택(Stack)처럼 맨 처음 들어간 버스는 맨 마지막에 나옴
# 한 번 임시 주차장으로 이동했던 버스는 다시 원래의 주차장으로 이동할 수 없음

# 버스들이 번호 순서대로 출발하는 것이 불가능한 지 알아보기 위해,
# 그것을 증명할 수 있는 서로 다른 (i, j, k)의 케이스들을 몇 개나 찾을 수 있는 지 출력

import sys

input = sys.stdin.readline

N = int(input())
bus = list(map(int, input().split()))
table = [[0 for i in range(N + 1)] for i in range(N + 1)]

for i in range(N - 1, -1, -1):
    for j in range(1, N + 1):
        if bus[i] < j:
            table[j][i] = table[j][i + 1] + 1
        else:
            table[j][i] = table[j][i + 1]
answer = 0
for i in range(N):
    for j in range(i, N):
        if bus[i] < bus[j]:
            answer += table[bus[i]][j]
print(answer)
