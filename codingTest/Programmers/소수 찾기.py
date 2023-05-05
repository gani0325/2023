# 소수 찾기
# 한자리 숫자가 적힌 종이 조각이 흩어져있음
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내기

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수

# numbers는 길이 1 이상 7 이하인 문자열
# numbers는 0~9까지 숫자만으로 이루어져 있음
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있음

from itertools import permutations


def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per = []

    for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))        # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per]   # 각 순열조합을 하나의 int형 숫자로 변환

    # 소수 확인
    for n in new_nums:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈
            if n % i == 0:
                check = False
                break
        if check:
            answer.append(n)                      # 소수일경우 answer 배열에 추가

    return len(set(answer))                       # set을 통해 중복 제거 후 반환
