"""
상담원 인원

💛 문제
현대모비스는 우수한 SW 인재 채용을 위해 상시로 채용 설명회를 진행하고 있습니다. 
채용 설명회에서는 채용과 관련된 상담을 원하는 참가자에게 멘토와 1:1로 상담할 수 있는 기회를 제공합니다.
채용 설명회에는 멘토 n명이 있으며, 1~k번으로 분류되는 상담 유형이 있습니다. 
각 멘토는 k개의 상담 유형 중 하나만 담당할 수 있습니다. 
멘토는 자신이 담당하는 유형의 상담만 가능하며, 다른 유형의 상담은 불가능합니다. 
멘토는 동시에 참가자 한 명과만 상담 가능하며, 상담 시간은 정확히 참가자가 요청한 시간만큼 걸립니다.

참가자가 상담 요청을 하면 아래와 같은 규칙대로 상담을 진행합니다.
    상담을 원하는 참가자가 상담 요청을 했을 때, 
    참가자의 상담 유형을 담당하는 멘토 중 상담 중이 아닌 멘토와 상담을 시작합니다.
    
    만약 참가자의 상담 유형을 담당하는 멘토가 모두 상담 중이라면, 자신의 차례가 올 때까지 기다립니다.
    참가자가 기다린 시간은 참가자가 상담 요청했을 때부터 멘토와 상담을 시작할 때까지의 시간입니다.

    모든 멘토는 상담이 끝났을 때 자신의 상담 유형의 상담을 받기 위해 기다리고 있는 참가자가 있으면 즉시 상담을 시작합니다. 
    이때, 먼저 상담 요청한 참가자가 우선됩니다.

참가자의 상담 요청 정보가 주어질 때, 
참가자가 상담을 요청했을 때부터 상담을 시작하기까지 기다린 시간의 합이 최소가 되도록 
각 상담 유형별로 멘토 인원을 정하려 합니다. 
단, 각 유형별로 멘토 인원이 적어도 한 명 이상이어야 합니다.

🧡 제한 사항
1 ≤ k ≤ 5
k ≤ n ≤ 20
3 ≤ reqs의 길이 ≤ 300
    reqs의 원소는 [a, b, c] 형태의 길이가 3인 정수 배열이며, c번 유형의 상담을 원하는 참가자가 a분에 b분 동안의 상담을 요청했음을 의미합니다.
    1 ≤ a ≤ 1,000
    1 ≤ b ≤ 100
    1 ≤ c ≤ k
    reqs는 a를 기준으로 오름차순으로 정렬되어 있습니다.
    reqs 배열에서 a는 중복되지 않습니다. 즉, 참가자가 상담 요청한 시각은 모두 다릅니다.

💚 입출력
k	n	reqs	                                                            result
3	5	[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1],  25
        [60, 30, 2], [65, 30, 1], [70, 100, 2]]	
2	3	[[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]	90
"""

# combinations(iterable, r) : 원소의 수가 r개인 조합
# combinations_with_replacement(iterable, r) : 원소의 수가 r개인 중복 조합
# permutations(iterable, r) : 몇 개를 골라 순서를 고려해 나열한 경우의 수 (순열)
# heap 이용해 상담 시간이 빠르게 끝나는 멘토와 대기자의 상담 시간을 비교하여 대기 시간 구하기

import heapq
from itertools import combinations_with_replacement, permutations

# 상담 유형의 수 k, 멘토의 수 n, 참가자의 상담 요청을 담은 2차원 정수 배열 reqs
def solution(k, n, reqs):
    answer = 1e9

    consulting = [[] for _ in range(k)]
    # [a, b, c] 형태의 길이가 3인 정수 배열
    # c번 유형의 상담을 원하는 참가자가 a분에 b분 동안의 상담을 요청
    for i in reqs:
        # consulting[유형별] = [시간, 상담시간]
        # [[[10, 60], [20, 30], [50, 40], [65, 30]], [[60, 30], [70, 100]], [[15, 100], [30, 50]]]
        consulting[i[2] - 1].append([i[0], i[1]])
    # 멘토 배치
    mento = set()
    # 최소 각 유형에 나올 수 있는 멘토 수 (각 유형별로 멘토 인원이 적어도 한 명 이상이어야 함)
    arr = [i for i in range(1, n - k + 2)]    
    
    # ex) k = 3 이라면, 중복 조합 -> (1, 1, 3), (1, 2, 2) ...
    for mem in combinations_with_replacement(arr, k):
        # 최소 각 유형에 나올 수 있는 멘토 수 & 중복 조합 된 경우의 수 합이 멘토 수와 같은지
        if mem not in mento and sum(mem) == n:
            # 가능한 모든 순서를 반환 (순열)
            for p in permutations(mem, k):
                mento.add(p)
    print(consulting)
    # mento : {(1, 1, 3), (1, 3, 1), (1, 2, 2), (2, 1, 2), (2, 2, 1), (3, 1, 1)}
    for case in mento:
        result = 0

        for i in range(k):
            # 멘토의 수 [0], [0, 0, 0] ...
            heap = [0] * case[i]
            
            # consulting[상담 유형] : [시간, 상담 시간]
            for startTime, consultingTime in consulting[i]:
                # 모든 값을 pop한 결과를 보면, 작은 값 순서(오름차순)로 출력된 것
                prev = heapq.heappop(heap)
                # 시작시간이 이전 종료 시간보다 작다면 바로 진행
                if startTime >= prev:
                    # 추가된 원소가 부모보다 작으면 (최소) 힙 구조가 아니므로, 부모와 자리를 바꾼다
                    heapq.heappush(heap, startTime + consultingTime)
                # 대기 시간 추가
                else:    
                    result += prev - startTime
                    heapq.heappush(heap, prev + consultingTime)
        
        # 중복조합 + 순열로 구한 "멘토 배열의 조합" 중에서, 가장 작은 대기 시간
        answer = min(answer, result)

    return answer