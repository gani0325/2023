# 의상
# 코니는 매일 다른 옷을 조합하여 입는것을 좋아함
# 각 종류별로 최대 1가지 의상만 착용
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산
# 코니는 하루에 최소 한 개의 의상은 입음

# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return
#   clothes의 각 행은 [의상의 이름, 의상의 종류]
#   코니가 가진 의상의 수는 1개 이상 30개 이하
#   같은 이름을 가진 의상은 존재하지 않음
#   clothes의 모든 원소는 문자열
#   모든 문자열의 길이는 1 이상 20 이하인 자연수, 알파벳 소문자 또는 '_'

def solution(clothes):
    closet = {}
    answer = 1
    for i in clothes:
        # 종류
        key = i[1]
        value = i[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    for i in closet.keys():
        # 모든 경우의 수 - 아예 안입은 거
        answer = answer * (len(closet[key]) + 1)
        answer -= 1
    return answer
