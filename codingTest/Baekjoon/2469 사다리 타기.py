"""
[2469] 사다리 타기

💛 문제
k명의 참가자들이 사다리 타기를 통하여 어떤 순서를 결정한다.
참가자들은 알파벳 대문자 첫 k개로 표현되며,
사다리 타기를 시작할 때의 순서는 아래 그림과 같이 항상 알파벳 순서대로이다.

k=10 인 예를 들어 보자.
10명의 A, B, C, D, E, F, G, H, I, J 참가자들이 사다리 타기를 준비한다.

아래 그림은 10개의 세로 줄과 5개의 가로 줄을 가지고 있는 사다리의 한 예를 보여주고 있다.

이 사다리에서 점선은 가로 막대가 없음을, 굵은 가로 실선은 옆으로 건너갈 수 있는 가로 막대가 있음
제시된 사다리를 타면 그 최종 도달된 순서는 왼쪽으로부터 A, C, G, B, E, D, J, F, I, H 가 된다.

사다리 타기는 세로 막대를 타고 내려오는 중에 가로막대를 만나면 그 쪽으로 옮겨 가면서 끝까지 내려가는 과정이다.
사다리 타기의 규칙 특성상 두 가로 막대가 직접 연결될 수는 없으므로 이 상황은 이 문제에서 고려할 필요가 없다.

우리는 하나의 가로 줄이 감추어진 사다리를 받아서
그 줄의 각 칸에 가로 막대를 적절히 넣어서 참가자들의 최종 순서가 원하는 순서대로 나오도록 만들려고 한다.

입력에서 사다리의 전체 모양은 각 줄에 있는 가로 막대의 유무로 표현된다.
각 줄에서 가로 막대가 없는 경우에는 ‘*’(별)문자, 있을 경우에는 ‘-’(빼기) 문자로 표시된다.
그리고 감추어진 특정 가로 줄은 길이 k-1인 ‘?’ (물음표) 문자열로 표시되어 있다.

💚 입력
첫 줄에는 참가한 사람의 수 k가 나온다(3 ≤ k ≤ 26).
그 다음 줄에는 가로 막대가 놓일 전체 가로 줄의 수를 나타내는 n이 나온다(3 ≤ n ≤ 1,000).
세 번째 줄에는 사다리를 타고 난 후 결정된 참가자들의 최종 순서가 길이 k인 대문자 문자열로 들어온다.
이어지는 n개의 줄에는 앞서 설명한 바와 같이 ‘*’와 ‘-’ 문자로 이루어진 길이 k-1인 문자열이 주어진다.
그 중 감추어진 가로 줄은 길이가 k-1인 ‘?’ 문자열로 표시되어 있다.

💙 출력
입력 파일 세 번째 줄에서 지정한 도착순서가 해당 사다리에서 만들어질 수 있도록 감추어진 가로 줄을 구성해야 한다.
감추어진 가로 줄의 상태를 재구성하여 이를 ‘*’(별) 문자와 ‘-’(빼기) 문자로 구성된 길이 k-1인 문자열로 만들어 출력하면 된다.

그런데 어떤 경우에는 그 감추어진 가로 줄을 어떻게 구성해도 원하는 순서를 얻을 수 없는 경우도 있다.
이 경우에는  ‘x’(소문자 엑스)로 구성된 길이 k-1인 문자열을 출력해야 한다.
"""

# 참가한 사람의 수
k = int(input())
# 가로 막대가 놓일 전체 가로 줄의 수
n = int(input())
# 사다리를 타고 난 후 결정된 참가자들의 최종 순서가 길이 (대문자 문자)
ladder = list(input())
# ‘*’와 ‘-’ 문자로 이루어진 길이 k-1인 문자열
graph = []
for i in range(n):
    graph.append(list(input()))

up = [[-1] * k for _ in range(n)]
down = [[-1] * k for _ in range(n)]
for i in range(k):
    up[0][i] = i
    down[-1][i] = ord(ladder[i]) - 65


def up_ladder():
    for i in range(n):
        if (graph[i][0] == '?'):
            temp = up[i]
            return temp

        else:
            for j in range(k-1):
                if j > 0 and j < k - 2:
                    if (graph[i][j] == '-'):
                        up[i+1][j+1] = up[i][j]
                    elif (graph[i][j-1] == '-'):
                        up[i+1][j-1] = up[i][j]
                    else:
                        up[i+1][j] = up[i][j]
                elif j == k-2:
                    if (graph[i][j-1] == '-'):
                        up[i+1][j-1] = up[i][j]
                        up[i+1][j+1] = up[i][j+1]
                    elif (graph[i][j] == '-'):
                        up[i+1][j] = up[i][j+1]
                        up[i+1][j+1] = up[i][j]
                    else:
                        up[i+1][j+1] = up[i][j+1]
                        up[i+1][j] = up[i][j]
                else:
                    if (graph[i][j] == '-'):
                        up[i+1][j+1] = up[i][j]
                    else:
                        up[i+1][j] = up[i][j]


def down_ladder():
    temp = []
    for i in range(n-1, -1, -1):
        if (graph[i][0] == '?'):
            temp = down[i]
            return temp
        for j in range(k-1):
            if j > 0 and j < k - 2:
                if (graph[i][j] == '-'):
                    down[i-1][j+1] = down[i][j]
                elif (graph[i][j-1] == '-'):
                    down[i-1][j-1] = down[i][j]
                else:
                    down[i-1][j] = down[i][j]
            elif j == k-2:
                if (graph[i][j-1] == '-'):
                    down[i-1][j-1] = down[i][j]
                    down[i-1][j+1] = down[i][j+1]
                elif (graph[i][j] == '-'):
                    down[i-1][j] = down[i][j+1]
                    down[i-1][j+1] = down[i][j]
                else:
                    down[i-1][j+1] = down[i][j+1]
                    down[i-1][j] = down[i][j]
            elif j == 0:
                if (graph[i][j] == '-'):
                    down[i-1][j+1] = down[i][j]
                else:
                    down[i-1][j] = down[i][j]


up_temp = up_ladder()
down_temp = down_ladder()

answer = []
for i in range(k-1):
    if up_temp[i] == down_temp[i]:
        answer.append("*")
    else:
        # 다리 놔주기
        if up_temp[i] == down_temp[i+1]:
            answer.append("-")
        # 이어주기
        elif i != 0 and up_temp[i] == down_temp[i-1]:
            answer.append("*")
        else:
            answer = ['x' for _ in range(k-1)]
            break

print(''.join(answer))
