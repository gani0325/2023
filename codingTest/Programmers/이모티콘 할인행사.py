"""
이모티콘 할인행사

💛 문제
카카오톡에서는 이모티콘을 무제한으로 사용할 수 있는 이모티콘 플러스 서비스 가입자 수를 늘리려고 합니다.
이를 위해 카카오톡에서는 이모티콘 할인 행사를 하는데, 목표는 다음과 같습니다.

이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
이모티콘 판매액을 최대한 늘리는 것.
1번 목표가 우선이며, 2번 목표가 그 다음입니다.

이모티콘 할인 행사는 다음과 같은 방식으로 진행됩니다.

n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매합니다.
이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
카카오톡 사용자들은 다음과 같은 기준을 따라 이모티콘을 사거나, 이모티콘 플러스 서비스에 가입합니다.

각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다.
각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 
이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입합니다.

카카오톡 사용자 n명의 구매 기준을 담은 2차원 정수 배열 users, 이모티콘 m개의 정가를 담은 1차원 정수 배열 emoticons
행사 목적을 최대한으로 달성했을 때의 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액을 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해주세요.


🧡 제한 사항
제한사항
    1 ≤ users의 길이 = n ≤ 100
    users의 원소는 [비율, 가격]의 형태입니다.
    users[i]는 i+1번 고객의 구매 기준을 의미합니다.
    비율% 이상의 할인이 있는 이모티콘을 모두 구매한다는 의미입니다.
        1 ≤ 비율 ≤ 40
    가격이상의 돈을 이모티콘 구매에 사용한다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입한다는 의미입니다.
        100 ≤ 가격 ≤ 1,000,000
        가격은 100의 배수입니다.
1 ≤ emoticons의 길이 = m ≤ 7
    emoticons[i]`는 i+1번 이모티콘의 정가를 의미합니다.
    100 ≤ emoticons의 원소 ≤ 1,000,000
    emoticons의 `원소는 100의 배수입니다.


💚 입출력
users	                                emoticons	                result
[[40, 10000], [25, 10000]]	            [7000, 9000]	            [1, 5400]
[[40, 2900], [23, 10000], 	            [1300, 1500, 1600, 4900]	[4, 13860]
[11, 5200], [5, 5900], 
[40, 3100], [27, 9200], [32, 6900]]
"""

# 중복순열(itertools의 product)
from itertools import product

def solution(users, emoticons):
    answer = []
    # 이모티콘의 할인율
    sales = [10, 20, 30, 40]    

    # tertools.product('ABCD', repeat=2)
    # 결과: AA AB AC AD BA BB BC BD CA CB => 중첩된 for loop에 해당하는 데카르트의 곱

    for i in product(sales, repeat=len(emoticons)): 
        # 가입자 수, 이모티콘 구매 가격 누적
        result = [0, 0]
        # users : [비율, 가격]
        for user in users:
            temp = 0   
            for j, k in enumerate(i):
                # 이모티콘 할인율이 유저가 원하는 할인율 이상이면 구매
                if k >= user[0]:    
                    temp += emoticons[j] * (100 - k) // 100

            # 유저 가격보다 초과하는 경우 이모티콘 플러스에 가입
            if temp >= user[1]:    
                result[0] += 1    # 가입자 카운트 +1
            else:
                result[1] += temp    # 이모티콘 구매 가격 누적

        # 해당 할인율 경우에서 구한 결과값을 answer에 추가
        answer.append(result)

    # 가입자 최대, 이모티콘 판매액 최대로 정렬
    answer.sort(key=lambda x: (-x[0], -x[1]))    
    # 가장 최대 첫 번째 출력
    return answer[0]