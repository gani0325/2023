"""
[16719] ZOAC

💛 문제
2018년 12월, 처음 시작하게 된 ZOAC의 오프닝을 맡은 성우는 누구보다 화려하게 ZOAC를 알리려 한다.
앞 글자부터 하나씩 보여주는 방식은 너무 식상하다고 생각한 성우는 문자열을 보여주는 새로운 규칙을 고안해냈다!
규칙은 이러하다. 아직 보여주지 않은 문자 중 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 하는 문자를 보여주는 것이다.
예를 들어 ZOAC를 보여주고 싶다면, A → AC → OAC → ZOAC 순으로 보여주면 된다.
바쁜 성우를 위하여 이 규칙대로 출력해주는 프로그램을 작성하시오.

💚 입력
첫 번째 줄에 알파벳 대문자로 구성된 문자열이 주어진다. 문자열의 길이는 최대 100자이다.

💙 출력
규칙에 맞게 순서대로 문자열을 출력한다.
"""

import sys
string = list(input())
temp = [[0]*2 for _ in range(len(string))]

# ZOAC : [(90, 0), (79, 1), (65, 2), (67, 3)]
# for i in range(len(string)):
#     temp[i] = ord(string[i]), i

# temp.sort(key=lambda x: (x[0], -x[1]))
# print(temp)  # => [(65, 2), (67, 3), (79, 1), (90, 0)]

result = [''] * len(string)


def func(arr, start):
    if not arr:
        return
    _min = min(arr)
    idx = arr.index(_min)
    result[start+idx] = _min

    print("".join(result))
    func(arr[idx+1:], start+idx+1)
    func(arr[:idx], start)

func(string, 0)