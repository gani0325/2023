# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수

# clothes의 각 행은 [의상의 이름, 의상의 종류]
# 같은 이름을 가진 의상은 존재하지 않음
# clothes의 모든 원소는 문자열
# 스파이는 하루에 최소 한 개의 의상 입음

def solution(clothes):
    closet = {}
    answer = 1
    
    # 같은 종류의 옷끼리 저장
    for cloth in clothes :
        # 옷 사전에 있다면
        if cloth[1] in closet.keys() :
            closet[cloth[1]].append(cloth[0])
        else :
            closet[cloth[1]] = [cloth[0]]
    
    # 경우의 수
    # 종류별로 옷을 0개 혹은 1개
    for value in closet.values() :
        answer *= len(value) + 1
    # {"headgear":["yellow_hat","green_turban"],"eyewear":["blue_sunglasses"]}
    
    # => 아무것도 안입음 + 하나만 + 종류별~
    # -1 해준다
    return answer - 1