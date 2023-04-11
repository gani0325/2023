# 달리기 경주
# 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부른다
# 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 
# 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
# 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성

def solution(players, callings):
    # 선수 이름 : 등수(인덱스)
    # {"mumu":0,"soe":1,"poe":2,"kai":3,"mine":4}
    play = {name : i for i, name in enumerate(players)}
    
    for i in callings :
        # key 넣음으로써 배열 위치 알게 됨
        call = play[i]
        players[call], players[call - 1] = players[call - 1], players[call]
        play[players[call]] = call
        play[players[call-1]] = call - 1
    return players