# 카펫
# 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫

# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return
#   카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다

def solution(brown, yellow):
    # 카펫 넓이
    total = brown + yellow

    # 가로 a, 세로 b
    for a in range(total, 2, -1):
        if total % a == 0:
            b = total // a
            # 테두리길이(2)만큼 빼주고 면적을 구함
            # yellow의 면적과 같다면 return
            if yellow == (b-2) * (a-2):
                return [a, b]
