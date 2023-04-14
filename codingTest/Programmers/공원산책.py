# 공원 산책
# 지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책
# 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행
#   ["방향 거리", "방향 거리" … ]
#   "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동
#   주어진 방향으로 이동할 때 공원을 벗어나는지 확인
#   주어진 방향으로 이동 중 장애물을 만나는지 확인
# 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행
# 공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1)

# 공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 
# 로봇 강아지가 모든 명령 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열 담아 return 하도록 solution 함수

from collections import deque

def solution(park, routes):
    # park : S 시작 지점, O 이동 가능한 통로, X 장애물
    # routes의 각 원소는 로봇 강아지가 수행할 명령어
    #       p : N 북쪽, S 남쪽, W 서쪽, E 동쪽
    answer = []
    queue = deque()
    map = []
    x = 0
    y = 0
    k = 0
    for i in range(len(park)) :
        temp = []
        for j in park[i] :
            temp.append(j)            
            if j == "S" :
                x = i
                y = k
            k += 1
        map.append(temp)

    for i in routes :
        a, b = i.split(" ")
        b = int(b)
        queue.append((a, b))
	# map : [['S', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
	# queue : deque([('E', 2), ('S', 2), ('W', 1)])
    # x, y : 0, 0
    
    # n 북, s 남, w 서, e 동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue :
        p, q = queue.popleft()
        m = len(map)
        n = len(i)
        if p == "N" :
            for z in range(1, q+1) :
                nx = x + dx[0] * z
                ny = y + dy[0] * z
                if 0 > nx or nx >= m or 0 > ny or ny >= n :
                    nx = x
                    ny = y
                    break
                if map[nx][ny] == "X" :
                    nx = x
                    ny = y
                    break
        elif p == "S" :
            for z in range(1, q+1) :
                nx = x + dx[1] * z
                ny = y + dy[1] * z
                if 0 > nx or nx >= m or 0 > ny or ny >= n :
                    nx = x
                    ny = y
                    break
                if map[nx][ny] == "X" :
                    nx = x
                    ny = y
                    break
        elif p == "W" :
            for z in range(1, q+1) :
                nx = x + dx[2] * z
                ny = y + dy[2] * z
                if 0 > nx or nx >= m or 0 > ny or ny >= n :
                    nx = x
                    ny = y
                    print(nx, ny)
                    break
                if map[nx][ny] == "X" :
                    nx = x
                    ny = y
                    print(nx, ny)
                    break
        elif p == "E" :
            for z in range(1, q+1) :
                nx = x + dx[3] * z
                ny = y + dy[3] * z
                if 0 > nx or nx >= m or 0 > ny or ny >= n :
                    nx = x
                    ny = y
                    break
                if map[nx][ny] == "X" :
                    nx = x
                    ny = y
                    break
        x, y = nx, ny
        answer = [x, y]
    return answer