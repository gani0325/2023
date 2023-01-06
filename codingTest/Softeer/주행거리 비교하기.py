# 두 차량 A와 B의 주행거리가 자연수로 주어졌을 때,
# 주행거리를 비교해서 어느 차량의 주행거리가 더 큰지 알아보자

import sys

A, B = map(int, input().split())

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("same")
