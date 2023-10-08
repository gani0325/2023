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

string = list(input())
visited = [False] * len(string)


def zoac(left, right):
    if left == right:
        return

    # 가장 작은 문자열 탐색
    minStr = min(string[left:right])
    minIndex = string[left:right].index(minStr) + left

    visited[minIndex] = True

    # 사전순으로 먼저 나오는 알파벳 순서로 출력
    for i in range(len(string)):
        if visited[i]:
            print(string[i], end='')
    print()

    # 찾은 문자 기준으로 앞, 뒤 탐색
    zoac(minIndex + 1, right)
    zoac(left, minIndex)


zoac(0, len(string))