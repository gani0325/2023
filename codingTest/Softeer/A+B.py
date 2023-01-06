# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성
import sys

input = sys.stdin.readline

T = int(input())
table = []
for i in range(T):
    a, b = map(int, input().split())
    table.append(a + b)

for i in range(T):
    print("Case #%d: %d" % (i + 1, table[i]))
