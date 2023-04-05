# codetree 참고함
# 격자 숫자 놀이
# 크기가 3 * 3인 격자판
# 놀이에 필요한 연산
# 1. 행의 개수가 열의 개수보다 크거나 같은 경우
# a. 모든 행에 대하여 정렬을 수행 (정렬 기준은 출현 빈도 수가 적은 순서대로 정렬)
# b. 출현하는 횟수가 같은 숫자가 있는 경우에는 해당 숫자가 작은 순서대로 정렬을 수행
# c. 정렬을 수행할 때 (숫자와 해당하는 숫자의 출현 빈도 수)를 함께 출력
# 2. 행의 개수가 열의 개수보다 작은 경우
# a. 모든 열에 대해 위의 과정을 수행
# 3. 행이나 열의 길이가 100을 넘어가는 경우에는 처음 100개의 격자를 제외하고는 모두 버림

# 변화된 격자의 크기는 가장 큰 길이를 기준으로 맞추고 나머지는 0을 채워줌 -> 한 번의 연산에 해당하고 총 1초
# 연산을 수행할 때는 0을 무시하고 수행

# 해당 격자판의 r번째 행의 c번째 열의 숫자를 A[r][c]라고 할 때, 
# 특정 A[r][c]의 값이 원하는 값이 되는데까지 걸리는 시간을 구하는 프로그램

# 첫번째 줄에는 목표 위치 r, c와 목표 숫자 k
# 두번째 줄부터 4번째 줄까지 배열 A에 있는 수

# 크기가 3 * 3인 격자판
n, m = 3, 3
# 목표 위치 r, c와 목표 숫자 k
r, c, k = map(int, input().split())
grid = [[0 for _ in range(100 + 1)] for _ in range(100 + 1)]

# row 행에 대해 숫자 놀이
def row_play(row):
    # 각 숫자에 대해 빈도수
    # 정렬시 빈도수, 숫자 순으로 오름차순 정렬이 되도록(빈도수, 숫자) 형태로 저장
    pairs = []
    frequency = 0
    for num in range(1, 100 + 1):
        for col in range(1, m+1) :
            if grid[row][col] == num :
                frequency += 1        
        if frequency:
            # 빈도수, 숫자 순으로 오름차순 정렬
            pairs.append((frequency, num))
    
    # 기존 row 행에 있던 숫자들을 전부 0
    for col in range(1, m + 1):
        grid[row][col] = 0
    
    pairs.sort()
    
    # row 행에 새로운 숫자를 차례대로 적기
    # (숫자와 해당하는 숫자의 출현 빈도 수)
    for i, (frequency, num) in enumerate(pairs):
        grid[row][i * 2 + 1] = num
        grid[row][i * 2 + 2] = frequency
    return grid
print(row_play(3))

pairs = []
frequency = 0
for num in range(1, 100 + 1):
    for col in range(1, m+1) :
        if grid[row][col] == num :
            frequency += 1        
    if frequency:
        # 빈도수, 숫자 순으로 오름차순 정렬
        pairs.append((frequency, num))

# 기존 row 행에 있던 숫자들을 전부 0
for col in range(1, m + 1):
    grid[row][col] = 0

pairs.sort()

# row 행에 새로운 숫자를 차례대로 적기
# (숫자와 해당하는 숫자의 출현 빈도 수)
for i, (frequency, num) in enumerate(pairs):
    grid[row][i * 2 + 1] = num
    grid[row][i * 2 + 2] = frequency
print(grid)