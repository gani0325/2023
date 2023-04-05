# 이차원 배열과 연산
# 크기가 3×3인 배열 A
# 배열의 인덱스는 1부터 시작
# 1초가 지날때마다 배열에 연산이 적용
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행
#     행의 개수 ≥ 열의 개수인 경우에 적용
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행
#     행의 개수 < 열의 개수인 경우에 적용

# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야함
# 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
# 배열 A에 정렬된 결과를 다시 넣어야 함
# 정렬된 결과를 배열에 넣을 때는, (수와 등장 횟수)를 모두 넣으며, 순서는 수가 먼저

# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버림
# 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간

# 첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)
# 둘째 줄부터 3개의 줄에 배열 A에 들어있는 수
# 배열 A에 들어있는 수는 100보다 작거나 같은 자연수

MAX_N = 100
MAX_NUM = 100

# 처음에는 3 x 3 이다
n, m = 3, 3
# A[r][c]에 들어있는 값이 k
r, c, k = map(int, input().split())
arr = [[0] * 101 for _ in range(101)]

# row 행에 대해 숫자 놀이
def row_play(row):
    # 각 숫자에 대해 빈도수
    # 정렬시 빈도수, 숫자 순으로 오름차순 정렬이 되도록
    # (빈도수, 숫자)
    pairs = []
    frequency = 0
    for num in range(1, 100 + 1):
        for col in range(1, m+1) :
            if arr[row][col] == num :
                frequency += 1        
        if frequency:
            # 빈도수, 숫자 순으로 오름차순 정렬
            pairs.append((frequency, num))

    # 숫자를 새로 적어줘야 하므로,
    # 그 전에 기존 row 행에 있던 숫자들을 전부 0
    for col in range(1, m + 1):
        arr[row][col] = 0
    # 오름차순 정렬
    pairs.sort()

    # row 행에 새로운 숫자를 차례대로
    for i, (frequency, num) in enumerate(pairs):
        arr[row][i * 2 + 1] = num
        arr[row][i * 2 + 2] = frequency

    return len(pairs) * 2


# col 열에 대해 숫자 놀이
def col_play(col):
    # 각 숫자에 대해 빈도수
    # 정렬시 빈도수, 숫자 순으로 오름차순 정렬
    # (빈도수, 숫자) 형태로 저장
    pairs = []
    frequency = 0
    for num in range(1, 100 + 1):
        for row in range(1, m+1) :
            if arr[row][col] == num :
                frequency += 1        
        if frequency:
            # 빈도수, 숫자 순으로 오름차순 정렬
            pairs.append((frequency, num))

    # 숫자를 새로 적어줘야 하므로,
    # 그 전에 기존 col 열에 있던 숫자들을 전부 0
    for row in range(1, m + 1):
        arr[row][col] = 0
    pairs.sort()

    # col 열에 새로운 숫자를 차례대로
    for i, (frequency, num) in enumerate(pairs):
        arr[i * 2 + 1][col] = num
        arr[i * 2 + 2][col] = frequency
    return len(pairs) * 2

def simulate():
    global n, m
    # 행의 개수가 열의 개수와 일치하거나 더 많다면
    # 행 단위로 진행 후, 최대로 긴 열의 크기
    if n >= m:
        m = max([row_play(row) for row in range(1, n + 1)])
    # 열의 개수가 더 많다면
    # 열 단위로 진행 후, 최대로 긴 행의 크기
    else:
        n = max([col_play(col) for col in range(1, m + 1)])

for i in range(1, n + 1):
    given_row = list(map(int, input().split()))
    # 쭊~~쭉~~ 입력 받은 list 넣기
    for j, elem in enumerate(given_row, start=1):
        arr[i][j] = elem

ans = -1
# 최대 100초 동안 시뮬레이션
for t in range(0, 100):
    if arr[r][c] == k:
        ans = t
        break
    simulate()
print(ans)