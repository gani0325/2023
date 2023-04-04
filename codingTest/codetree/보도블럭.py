# codetree 참고함
# 보도블럭
# 크기가 n * n인 인도 (인도의 각 칸에는 해당 칸의 보도블럭의 높이)
# 보도블럭의 크기가 일정하지 않음 -> 경사로를 설치
# 경사로는 높이가 1이며 길이 L

# 경사로를 설치할 수 있는 조건
# 1. 경사로는 높이 차이가 1이 나는 보도블럭에 설치가능하며, 낮은 칸에 설치
# 2. 경사로의 길이 L동안 바닥에 접촉해야하며, 경사로가 놓인 보도블럭의 높이는 모두 같아야 함

# 경사로를 놓을 수 없는 조건
# 높이가 1 이상 차이 나는 경우
# 경사로의 길이만큼 낮은 칸의 보도블럭이 연속하지 않는 경우
# 경사로를 놓은 곳에 또 경사로를 놓은 경우

# 특정 열이나 행에 속한 모든 보도블럭의 높이가 같거나 경사로를 설치하여 지나갈 수 있게 만들어져있음

# 인도와 경사로의 정보가 격자판으로 주어질 때 지나갈 수 있는 열과 행의 총 개수를 출력하는 프로그램

# 첫째 줄에 보도블럭의 크기 n과 연결할 수 있는 경사로의 길이 L
# 두번째 줄부터 (n+1)번째 줄까지 보드블럭의 높이 정보가 숫자

# n * n인 인도, 경사로는 높이가 1이며 길이 L
n, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 지날 수 있는 길의 경우들
arr = [0 for _ in range(n)]   
count = 0   # 가능한 길

# 각 칸마다 경사로가 몇 번씩 놓여졌는지
# 경사로가 겹쳐 놓여지는지를 확인
ramp_cnt = [0 for _ in range(n)]

# arr의 [l, r] 구간에 있는 원소가 전부 동일한 원소인지
def all_same(l, r):
    return len(set(arr[l:r + 1])) == 1

# 해당 arr가 지나갈 수 있는 경우인지
def can_pass():
    global ramp_cnt
    
    # Step 1.
    # 인접한 곳의 높이 차가 2 이상인 곳이 있는지 
    # 존재한다면, 불가능
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) >= 2:
            return False
    
    # 각 위치마다 경사로의 개수를 0으로 초기화
    ramp_cnt = [0 for _ in range(n)]
    
    # Step2. 꼭 놓아야 할 경사로를 확인
    # Step2-1. ◣ 직각삼각형이 필요한 곳을 찾기
    for i in range(n - 1):
        # [i + 1, i + L] 까지 경사로를 놓아야만 하는 경우
        if arr[i] == arr[i + 1] + 1:
            # L만큼의 여유 공간이 있는지 확인
            # 없다면 불가능
            if i + L >= n:
                return False
            
            # 경사로가 놓일 곳의 높이가 전부 같은지 확인
            # 전부 같지 않다면 불가능
            if not all_same(i + 1, i + L):
                return False
            
            # 경사로가 놓이는 곳에 개수를 갱신
            for j in range(i + 1, i + L + 1):
                ramp_cnt[j] += 1
				
	# Step2-2. ◢ 직각삼각형이 필요한 곳을 찾기
    for i in range(1, n):
        # [i - L, i - 1] 까지 경사로를 놓아야만 하는 경우
        if arr[i] == arr[i - 1] + 1:
            # L만큼의 여유 공간이 있는지 확인
            # 없다면 불가능
            if i - L < 0:
                return False
            
            # 경사로가 놓일 곳의 높이가 전부 같은지 확인
            # 전부 같지 않다면 불가능
            if not all_same(i - L, i - 1):
                return False
            
            # 경사로가 놓이는 곳에 개수를 갱신
            for j in range(i - L, i):
                ramp_cnt[j] += 1
    
    # Step3.
    # 꼭 놓아야 했던 경사로끼리 겹쳐 놓였는지 확인
    # 그랬다면, 불가능
    if any([cnt >= 2 for cnt in ramp_cnt]):
        return False
    
    # 모든 조건을 만족했다면, 가능한 경우
    return True

# row 번째 행이 지나갈 수 있는 곳인지 확인
for row in range(n):
    # 확인하고 싶은 수열을 입력
    for col in range(n):
        arr[col] = grid[row][col]

    # 지나갈 수 있다면 답을 갱신
    if can_pass():
        count += 1

# column번째 열이 지나갈 수 있는 곳인지 확인
for col in range(n):
    # 확인하고 싶은 수열을 입력
    for row in range(n):
        arr[row] = grid[row][col]

    # 지나갈 수 있다면 답을 갱신
    if can_pass():
        count += 1

print(count)