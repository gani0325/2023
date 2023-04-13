# 추억 점수
# 사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매기기
# 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수
#   사진 속 인물의 이름이 ["may", "kein", "kain"]이고 각 인물의 그리움 점수가 [5점, 10점, 1점
#   해당 사진의 추억 점수는 16(5 + 10 + 1)
# 그리워하는 사람의 이름을 담은 문자열 배열 name, 각 사람별 그리움 점수를 담은 정수 배열 yearning, 
# 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때, 
# 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수

def solution(name, yearning, photo):
    answer = []
    
    # 사진들 리스트 개수 만큼
    for i in range(len(photo)) :
        s = 0
        # 첫번째 사진의 추억 점수 합산
        for j in photo[i] :
            # name 에 해당하는 이름이 있다면
            if j in name :
                # 인덱스 번호를 통해 점수 합산
                temp = name.index(j)
                s += yearning[temp]
            # 해당 이름이 없다면 계속
            else :
                continue
        # 리스트 별로 합산 추가
        answer.append(s)
    return answer