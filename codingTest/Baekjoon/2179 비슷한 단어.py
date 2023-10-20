"""
[2179] 비슷한 단어

💛 문제
N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구해내는 프로그램을 작성하시오.

두 단어의 비슷한 정도는 두 단어의 접두사의 길이로 측정한다. 
접두사란 두 단어의 앞부분에서 공통적으로 나타나는 부분문자열을 말한다. 
즉, 두 단어의 앞에서부터 M개의 글자들이 같으면서 M이 최대인 경우를 구하는 것이다. 
"AHEHHEH", "AHAHEH"의 접두사는 "AH"가 되고, "AB", "CD"의 접두사는 ""(길이가 0)이 된다.

접두사의 길이가 최대인 경우가 여러 개일 때에는 입력되는 순서대로 제일 앞쪽에 있는 단어를 답으로 한다. 
즉, 답으로 S라는 문자열과 T라는 문자열을 출력한다고 했을 때, 
우선 S가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력하고, 
그런 경우도 여러 개 있을 때에는 그 중에서 T가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력한다.

💚 입력
첫째 줄에 N(2 ≤ N ≤ 20,000)이 주어진다.
다음 N개의 줄에 알파벳 소문자로만 이루어진 길이 100자 이하의 서로 다른 영단어가 주어진다.

💙 출력
첫째 줄에 S를, 둘째 줄에 T를 출력한다. 
단, 이 두 단어는 서로 달라야 한다. 
즉, 가장 비슷한 두 단어를 구할 때 같은 단어는 제외하는 것이다.

9
noon
is
lunch
for
most
noone
waits
until
two
"""

n = int(input())

words = []

for _ in range(n):
    # ['noon', 'is', 'lunch', 'for', 'most', 'noone', 'waits', 'until', 'two']
    words.append(input())

ans = 0
word1, word2 = "", ""

for i in range(n):
    if len(words[i]) < ans:
        continue

    # 그다음부터 끝까지 비교
    for j in range(i + 1, n):

        # 작은 문자열 길이만큼 비교해야됨 (안그러면 list index 초과)
        length = min(len(words[i]), len(words[j]))

        if length < ans or words[i] == words[j]:
            continue

        cnt = 0
        for k in range(length):
            # 작은 문자열 길이만큼 비교하기
            if words[i][k] == words[j][k]:
                cnt += 1

            else:
                break

        if cnt > ans:
            # ans에 접두사 길이 대입 (클 때마다 갱신하기)
            word1, word2, ans = words[i], words[j], cnt

print(word1)
print(word2)
