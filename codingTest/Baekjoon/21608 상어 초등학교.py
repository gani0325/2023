# 상어초등학교
# 상어 초등학교에는 교실이 하나 있고, 교실은 N×N 크기의 격자
# 학교에 다니는 학생의 수는 N2명

# 모든 학생의 자리를 정하는 날
# 학생은 1번부터 N2번까지 번호가 매겨져 있고, (r, c)는 r행 c열을 의미
# 교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)

# 선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사
# 규칙을 이용해 정해진 순서대로 학생의 자리를 정하기
# 한 칸에는 학생 한 명의 자리만 있을 수 있고, r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다
#     1) 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
#     2) 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다
#     3) 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 
#         그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다
# 학생의 만족도를 구해야 한다
#     학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다
#     그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다
#     그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000

# 학생의 만족도의 총 합을 구해보자

# 첫째 줄에 N이 주어진다
# 둘째 줄부터 N2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다
#     학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생
#     학생의 번호, 좋아하는 학생의 번호는 N2보다 작거나 같은 자연수
#     어떤 학생이 자기 자신을 좋아하는 경우는 없다


# 교실은 N×N 크기의 격자
n = int(input())
# 학교에 다니는 학생의 수는 N^2명
p = n * n
classroom = [[0] * n for _ in range(n)]
# 각 학생 인덱스에 맞는 좋아하는 사람을 저장
like_room = [[] for _ in range(p + 1)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(p) :
    # 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호
    array = list(map(int, input().split()))
    # 각 학생 인덱스에 맞는 좋아하는 사람을 저장
    like = array[1:]
    # 학생의 번호 넣으면 그거에 맞는 좋아하는 학생 4명 나옴
    like_room[array[0]] = like
    if p == 0 :
        classroom[1][1] = array[0]
        continue
    
    temp = []
    for i in range(n) :
        for j in range(n) :
            sum_like, sum_empty = 0, 0
            if classroom[i][j] != 0 :
                continue
            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 :
                    continue
                # 해당 자리에서 인접한 곳에 좋아하는 학생있으면 +1
                if classroom[nx][ny] in like :
                    sum_like += 1
                # 인접한 곳이 빈 경우일 때 +1
                if classroom[nx][ny] == 0 :
                    sum_empty += 1
            # sum_like, sum_empty, (i,j => 해당 행,열값)
            temp.append((sum_like, sum_empty, (i, j)))
    # 좋아하는 사람 수 많은 칸 > 빈 칸 여러개 > 행 적은 곳 > 열 적은 곳
    temp.sort(key = lambda x : (-x[0], -x[1], x[2]))  # -를 붙이면, 현재와 반대로 정렬 (내림차순)
    # classroom 리스트의 해당 행, 열에 학생 번호로 변경
    classroom[temp[0][2][0]][temp[0][2][1]] = array[0]

sum_answer = 0
for i in range(n) :
    for j in range(n) :
        answer = 0
        # # 하나하나 인접 지역에 얼마나 좋아하는 학생이 배치되었는지 확인
        for k in range(4) :
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 :
                continue
            if classroom[nx][ny] in like_room[classroom[i][j]] :
                answer += 1
                continue
        if answer != 0 :
            # 학생의 만족도를 계산
            sum_answer += (10 ** (answer -1))
print(sum_answer) 