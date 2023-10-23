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

"""
분명 패턴이 있는데 이 패턴을 어떻게 정리하고 구현할지 고민하다가
K+1의 이진수에서 가장 큰 자리수를 없애면 매칭이 된다는 것을 알게 되었다. 
즉, K가 5일때 4와 7로 만들 수 있는 5번째 작은 수는 74인데 위의 그림에서 74를 7을 1로 표현하고 
4를 0으로 표현한 이진수로 보았을 때 10으로 되어있다. 
이때 5+1(=6)의 이진수는 110이고 여기서 가장 큰 자리수인 1을 없애면 10이 남는다. 
이 10이란 숫자를 다시 1은 7로, 0은 4로 변환해서 출력해주면 74가 된다.
https://syh39.github.io/algorithm/algorithm_BOJ_2877/
"""

# k + 1 한 후 이진수로 변환
bin_num = bin(k + 1)

# 이진수를 배열로 변환 + 가장 큰 자리수 없애기
temp = list(map(int, str(bin_num[3:])))

# 1을 7, 0을 4로 바꾼다
int_num = []
for i in range(len(temp)):
    if temp[i] == 1:
        int_num.append(7)
    else:
        int_num.append(4)

result = ''.join(map(str, int_num))
print(result)
