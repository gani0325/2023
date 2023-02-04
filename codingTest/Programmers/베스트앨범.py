# 속한 노래가 많이 재생된 장르를 먼저 수록
# 장르 내에서 많이 재생된 노래를 먼저 수록
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록

# genres [i]는 고유번호가 i인 노래의 장르
# plays [i]는 고유번호가 i인 노래가 재생된 횟수

# 노래의 장르를 나타내는 문자열 배열 genres와 
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수

def solution(genres, plays):
    answer = []
    # 전체 장르별 총 재생 횟수
    total_play = {}
    # 장르별 재생 횟수
    genres_play = {}
    
    for i in range(len(genres)) :
        # key 존재하면 횟수 증가
        if genres[i] in total_play :
            total_play[genres[i]] += plays[i]
        else :
        # 아니면 초기화
            total_play[genres[i]] = plays[i]
        
        # key 존재하면 추가
        if genres[i] in genres_play :
            genres_play[genres[i]].append([plays[i], i])
        else :
        # 아니면 [재생횟수, 인덱스]
            genres_play[genres[i]] = [[plays[i], i]]
    
    # value를 내림차순으로
    genres_rank = sorted(total_play, key = total_play.get, reverse = True)
    
    for x in genres_rank :
        # 재싱횟수(내림), 인덱스(오름)
        play_rank = sorted(genres_play[x], key = lambda x : (-x[0], x[1]))
        
        # 곡 하나면 하나만, 아니면 앞 2개
        # play_rank[i][1] index만 추가
        if len(play_rank) == 1 :
            answer.append(play_rank[0][1])
        else :
            for i in range(2) :
                answer.append(play_rank[i][1])
    return answer