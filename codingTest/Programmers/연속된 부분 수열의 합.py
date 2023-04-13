# 연속된 부분 수열의 합
# 비내림차순으로 정렬된 수열이 주어질 때, 다음 조건을 만족하는 부분 수열
#   기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열
#   부분 수열의 합은 k
#   합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾기
#   길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾기
# 수열을 나타내는 정수 배열 sequence와 부분 수열의 합을 나타내는 정수 k가 매개변수로 주어질 때, 
# 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return 하는 solution 함수
# 수열의 인덱스는 0부터 시작

# 수열을 나타내는 정수 배열 sequence, 부분 수열의 합 k
def solution(sequence, k):
    answer = []
    n = len(sequence)

    max_sum = 0
    end = 0
    res = []
    
    for i in range(n):
        # 부분 수열의 합이 k 될 때까지 합산하기
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        # 부분 수열의 합 k과 같다면
        if max_sum == k:
            # [시작점, 끝점, 길이] 
            res.append([i, end-1, end-1-i])

        max_sum -= sequence[i]
    # 길이 짧은 순으로 정렬
    res = sorted(res, key=lambda x: x[2])
    # [시작점, 끝점]
    return res[0][:2]