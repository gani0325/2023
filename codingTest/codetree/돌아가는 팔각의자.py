# codetree 참고함
# 돌아가는 팔각의자
# 총 4개의 팔각 의자에 두 지역에서 온 사람들이 앉아있음
# 각각 북부 지방과 남부 지방으로 N과 S로 표시
# 팔각 의자는 왼쪽에서부터 오른쪽까지 각각 1번부터 4번까지의 번호
# 각각의 의자를 총 k번 회전 -> 한 번 회전할 때 45도씩, 한 칸 움직임 (시계 방향, 반시계 방향 모두 가능)

# 회전요청 규칙
# 1. 회전시킬 의자의 번호와 방향
# 2. n번째 의자가 회전하기 전 인접한 의자(n-1번째와 n+1번쨰)에 있던 의자에서 
# 제일 가깝게 마주치는 두 명의 사람의 출신 지역이 다르다면
# n번째 의자가 회전할 때 인접한 의자 또한 반대 방향으로 회전
# 3. 회전 요청에 따라 의자를 회전시킨 후 그로 인해 일어나는 모든 회전이 끝날 때까지 기다림
# 한 번 회전한 의자는 다시 회전하지 않음

# 각 의자의 12시 방향에 앉아있는 남쪽 지방의 사람의 착석 여부를 알아내는 프로그램
# 12시 방향에 남쪽지방 사람 착석여부를 각 테이블에 대하여 s1, s2, s3, s4라고 할 때 
# 1*s1 + 2*s2 + 4*s3 + 8*s4를 출력 (착석시 1, 아니면 0)

# 첫번째 줄에는 첫번째 팔각 의자에 앉아있는 사람들의 지역
# 두번째 줄에는 두번째 팔각 의자에 앉아있는 사람들의 지역
# 세번째 줄에는 세번째 팔각 의자에 앉아있는 사람들의 지역
# 네번째 줄에는 네번째 팔각 의자에 앉아있는 사람들의 지역
# 각 지역은 12시 방향부터 시계 방향 순서대로 (0은 N 북쪽 지방, 1은 S 남쪽 지방)
# 다섯번째 줄에는 회전 횟수 k
# 6번째 줄부터 (k+5)번째 줄까지 회전시킬 팔각의자의 번호 n와 방향 d (1은 시계방향, -1은 반시계 방향)

NOT_ROTATE = 0

# 4개의 8각 의자
n, m = 4, 8
graph = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
# 의자별로 회전해야 할 방향 (1, -1)
rotate_dir = [0 for _ in range(n + 1)]

# 의자를 해당 방향으로 밀어줌
def shift(curr_num, curr_dir):
    # 시계방향으로 회전
    if curr_dir == 1:
        temp = graph[curr_num][m]
        for i in range(m, 1, -1):
            graph[curr_num][i] = graph[curr_num][i - 1]
        graph[curr_num][1] = temp
    
    # 반시계방향으로 회전
    else:
        temp = graph[curr_num][1]
        for i in range(1, m):
            graph[curr_num][i] = graph[curr_num][i + 1]
        graph[curr_num][m] = temp

# 주어진 방향으로부터 반대 방향의 값을 반환
def flip(curr_dir):
    return -1 if curr_dir == 1 else 1

def simulate(start_num, start_dir):
    global rotate_dir
    
    # Step1
    # 회전하게 되는 의자가 도는 방향이 동시에 결정되므로
    # 먼저 각 의자마다 회전하게 될 방향
    
    # 초기값은 전부 회전하지 않음으로 표시
    rotate_dir = [0 for _ in range(n + 1)]
    
    # 시작 위치는 반드시 회전
    rotate_dir[start_num] = start_dir
    
    # 좌측에 있는 의자들의 회전 방향을 정함
    # 마주보는 두 사람의 지역이 다를때만 반복하며, 그렇지 않은 경우에는 종료
    # 방향을 계속 뒤집어줘야 함에 유의
    for i in range(start_num - 1, 0, -1):
        if graph[i][3] != graph[i + 1][7]:
            rotate_dir[i] = flip(rotate_dir[i + 1])
        else:
            break
    
    # 우측에 있는 의자들의 회전 방향을 정함
    # 마주보는 두 사람의 지역이 다를때만 반복하며, 그렇지 않은 경우에는 종료
    # 방향을 계속 뒤집어줘야 함에 유의
    for i in range(start_num + 1, n + 1, 1):
        if graph[i][7] != graph[i - 1][3]:
            rotate_dir[i] = flip(rotate_dir[i - 1])
        else:
            break
    
    # Step2
    # step 1에 의해 회전이 결정된 의자들을 회전
    for i in range(1, n + 1):
        if rotate_dir[i] != 0:
            shift(i, rotate_dir[i])

for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start=1):
        graph[i][j] = elem

k = int(input())
for _ in range(k):
    start_num, start_dir = map(int, input().split())
    simulate(start_num, start_dir)

ans = 0
for i in range(1, n+1) :
    if graph[i][1] == "1" :
        ans += 2 ** (i - 1)

# 출력:
print(ans)

##################예제######################
"""
입력:
01000011
01100010
11100000
01000110
1
3 1

출력:
3
"""