# 마리오 게임
# 버섯을 규칙에 맞게 먹어서 키를 최대한 키우는 단순한 게임
# 가장 키를 많이 키운 사람이 우승이다

# 값범위
# 1. 버섯의 개수N (N=자연수, 1≤N≤150,000)
# 2. 버섯은 일렬로 늘어져있으며 0번부터 N-1번까지
# 3. 버섯에 써있는 숫자 P (P=자연수, 1≤P≤500)

# 버섯을먹는규칙
# 1. 버섯은 0번부터 순서대로 먹을지 먹지않을지 결정해야함
# 2. 첫 번째로 먹은 버섯의 숫자만큼 키가 커짐
# 3. 두 번째로 먹은 버섯의 숫자만큼 키가 작아짐
# 4. 즉, 홀수 번째로 먹은 버섯의 숫자만큼 커지고 짝수 번째로 먹은 숫자만큼 작아짐

# 버섯 수 N과 각 버섯의 값 P가 주어졌을 때, 마리오의 키를 최대한 키웠을 때의 값

# 첫 번째 줄에는 버섯 수 N
# 두 번째 줄에는 N 개의 버섯이 값 P가 공백으로 구분되어 입력 (0 ~ N-1)

# 버섯 수
n = int(input())
# 버섯
mush = list(map(int, input().split()))


def eat(n, mush):
    answer = 0
    k = 1
    for i in range(n):
        if i != n-1:
            # 짝수라면
            if k % 2 != 0:
                if mush[i] >= mush[i+1]:
                    answer += mush[i]
                    k += 1
                else:
                    pass
            # 홀수라면
            else:
                if mush[i] >= mush[i+1]:
                    answer -= mush[i]
                    k += 1
                else:
                    pass
        else:
            if k % 2 != 0:
                answer += mush[i]
                k += 1
    return answer
