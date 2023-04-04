# codetree 참고함
# 디버깅
# 고객들에게 알맞은 데이터가 전달되고 있는지 유지보수하는 일

# i번 줄의 결과는 무조건 i번으로 가야한다는 것
# 데이터가 제대로 옮겨지지 않는 경우를 버그
# 사다리 게임의 가로선에 해당하는 것은 메모리 유실선이 있을 수 있는 위치
# (취약 지점이라 하며 이웃한 선과만 이어질 수 있음)

# 최소한의 메모리 유실선을 추가해서 버그를 없애는 프로그램
# 필요한 선의 개수가 3보다 큰 값이거나 버그를 고치는 것이 불가능하다면 -1을 출력

# 첫 번째 줄에는 고객의 수 n, 메모리 유실 선의 개수 m, 취약 지점의 개수 h
# 두 번째 줄에서부터 m+1번째 줄까지 메모리 유실 선의 정보 (취약 지점과 메모리 유실이 일어난 지점)
# 취약 지점이 a, 메모리 유실이 일어난 지점을 b
# 고객의 번호는 1번부터 시작하며 오른쪽으로 갈수록 1씩 증가
# 취약지점의 번호도 1번부터 시작하며 아래쪽으로 갈수록 1씩 증가

import sys
INT_MAX = sys.maxsize
ans = INT_MAX

# 고객의 수 n, 메모리 유실 선의 개수 m, 취약 지점의 개수 h
n, m, h = map(int, input().split())
line = [[False for _ in range(n + 1)] for _ in range(h + 1)]

# i번째 줄이 어디로 향하는지 계산하기 위해 필요한 배열
num = [0 for _ in range(n + 1)]
candidates = []

#i번째 줄이 전부 i번으로 가는지 확인
def possible():
    # 유실 선끼리 이어져있는지 확인하고 그런 경우에는 불가능하다 판단
    if any([
        line[a][b] and line[a][b - 1]
        for a in range(1, h + 1)
        for b in range(2, n)
    ]):
        return False
    
    # 직접 어느 위치로 이동하는지를 계산하기 위해 초기값을 설정
    for i in range(1, n + 1):
        num[i] = i
	
    # 유실 선이 있는 경우 해당 위치에 있는 고객의 번호를 서로 교환
    for a in range(1, h + 1):
        for b in range(1, n):
            if line[a][b]:
                num[b], num[b + 1] = num[b + 1], num[b]
    
    # 전부 자기 자신으로 내려오는지 확인
    if any([
        num[i] != i
        for i in range(1, n + 1)
    ]):
        return False
    return True

def find_min(curr_idx, cnt):
    global ans
    
    # 추가한 유실선의 수가 이미 지금까지 구한 답보다 좋아질 수 없다면 퇴각
    if cnt >= ans:
        return
    
    # 가능한 조합이라면, 답을 갱신
    if possible():
        ans = min(ans, cnt)
    
    # 이미 3개를 뽑았거나, 더 이상 뽑을 게 없다면 퇴각
    if cnt == 3 or curr_idx == len(candidates):
        return

    # curr_idx 번째 유실선은 추가하지 않았을 경우
    find_min(curr_idx + 1, cnt)
    
    # curr_idx 번째 유실선을 추가헀을 경우 해당 위치에 유실선을 추가
    a, b = candidates[curr_idx]
    line[a][b] = True
    find_min(curr_idx + 1, cnt + 1)
    line[a][b] = False
    
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    line[a][b] = True
    
# 선을 놓을 수 있는 목록 생성
candidates = [
    (i, j)
    for i in range(1, h + 1)
    for j in range(1, n)
    if not line[i][j]
]

find_min(0, 0)

if ans == INT_MAX:
    ans = -1

# 출력:
print(ans)

##################예제######################
"""
입력:
4 3 5
1 1
3 2
5 1

출력:
1
"""