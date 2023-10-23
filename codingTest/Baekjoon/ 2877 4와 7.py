"""
[2877] 4와 7

💛 문제
창영이는 4와 7로 이루어진 수를 좋아한다. 
창영이가 좋아하는 수 중에 K번째 작은 수를 구해 출력하는 프로그램을 작성하시오.

💚 입력
첫째 줄에 K(1 ≤ K ≤ 10^9)가 주어진다.

💙 출력
첫째 줄에 창영이가 좋아하는 숫자 중 K번째 작은 수를 출력한다.
"""

# 중복 순열
from itertools import product

# K번째 작은 수
k = int(input())

numbers = [4, 7]

def pro (k, numbers) :
    cnt = 0
    result = []
    i = 0
    while (1) :
        i += 1
        # [(4,), (7,)]
        # [(4, 4), (4, 7), (7, 4), (7, 7)]
        # [(4, 4, 4), (4, 4, 7), (4, 7, 4), (4, 7, 7), (7, 4, 4), (7, 4, 7), (7, 7, 4), (7, 7, 7)]
        data = list(product(numbers, repeat=i))

        for j in range(len(data)) :
            cnt += 1

            if cnt == k :
                result = data[j]
                return result


answer = pro(k, numbers)
for x in answer:
    print(x, end="")