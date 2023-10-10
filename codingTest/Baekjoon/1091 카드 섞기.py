"""
[1091] 카드 섞기

💛 문제
지민이는 카지노의 딜러이고, 지금 3명의 플레이어(0, 1, 2)가 있다.
이 게임은 N개의 카드를 이용한다. (0 ~ N-1번)

일단 지민이는 카드를 몇 번 섞은 다음에, 그것을 플레이어들에게 나누어 준다.
0번째 위치에 있던 카드가 플레이어 0에게 가고,
1번째 위치에 있던 카드는 플레이어 1에게 가고,
2번째 위치에 있던 카드는 플레이어 2에게 가고,
3번째 위치에 있던 카드는 플레이어 0에게 가고,
이런식으로 카드를 나누어 준다. 하지만, 지민이는 약간 사기를 치려고 한다.

지민이는 처음에 카드를 섞기 전에 카드의 순서를 알고 있고,
이 정보를 이용해 각 카드가 특정한 플레이어에게 보내지게 할 것이다.

카드를 한 번 섞을 때는 주어진 방법을 이용해서만 섞을 수 있고,
이 방법은 길이가 N인 수열 S로 주어진다.
카드를 한 번 섞고 나면 i번째 위치에 있던 카드는 S[i]번째 위치로 이동하게 된다.

각 카드가 어떤 플레이어에게 가야 하는지에 대한 정보는 길이가 N인 수열 P로 주어진다.
맨 처음 i번째 위치에 있던 카드를 최종적으로 플레이어 P[i] 에게 보내야한다.

지민이가 목적을 달성하기 위해 필요한 카드 섞는 횟수의 최솟값을 구하는 프로그램을 작성하시오.

💚 입력
첫째 줄에 N이 주어진다. N은 3보다 크거나 같고, 48보다 작거나 같은 3의 배수이다.
둘째 줄에 길이가 N인 수열 P가 주어진다. 수열 P에 있는 수는 0, 1, 2 중 하나이다.
셋째 줄에 길이가 N인 수열 S가 주어진다. 수열 S에 있는 수는 모두 N-1보다 작거나 같은 자연수 또는 0이고 중복되지 않는다.

💙 출력
첫째 줄에 몇 번 섞어야 하는지 출력한다.
만약, 섞어도 섞어도 카드를 해당하는 플레이어에게 줄 수 없다면, -1을 출력한다.
"""

# N개의 카드
n = int(input())
# 길이가 N인 수열 P (0, 1, 2 중 하나)
p = list(map(int, input().split()))
# 길이가 N인 수열 S
s = list(map(int, input().split()))

result_temp = [[] for _ in range(3)]
p_temp = [[] for _ in range(3)]
s_temp = [[] for _ in range(n)]

# 처음 카드
init_card = [i for i in range(n)]

# 정답 카드 배열 => n = 6 일 때 [[0, 3], [1, 4], [2, 5]]
for i in range(n):
    result_temp[i % 3].append(i)

# p 수열대로 원하는 카드 배열 먼저 생성 => n = 6 일 때 [[0, 3], [1, 4], [2, 5]]
for i in range(n):
    p_temp[p[i]].append(init_card[i])

# s 수열대로 카드 섞기
def s_card(s_temp):
    ss_temp = [-1 for _ in range(n)]

    for i in range(n):
        ss_temp[s[i]] = s_temp[i]
    return ss_temp

# s 수열대로 한 후 카드 나누기
def p_card(ss_temp):
    pp_temp = [[] for _ in range(3)]
    for i in range(n):
        pp_temp[p[i]].append(ss_temp[i])

    ppp_temp = [[] for _ in range(3)]

    for i in range(n):
        pp_temp[i % 3].append(pp_temp[i])
    return ppp_temp


def card(sss_temp, result) :
    s_temp2 = [[] for _ in range(3)]
    p_temp2 = [[] for _ in range(3)]
    s_temp2 = s_card(sss_temp)
    p_temp2 = p_card(s_temp2)

    result += 1    
    if (p_temp2 == p_temp) :
        return result
    else :
        for _ in range(n) :           
            card(s_temp2, result)
        return -1

# 처음에는 그냥 섞어요
result = 0
if (result_temp == p_temp) :
    print(0)
else :
    s_temp = s_card(init_card)
    print(card(s_temp, result))
