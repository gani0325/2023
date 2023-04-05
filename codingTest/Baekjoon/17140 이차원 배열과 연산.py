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

arr = [[0] * 101 for _ in range(101)]

# A[r][c]에 들어있는 값이 k
r, c, k = map(int, input().split())
# 처음에는 3 x 3 이다
start_r = 3
start_c = 3
for i in range(1, 4):
    aa, bb, cc = map(int, input().split())
    # 넣어 버섯~
    arr[i][1] = aa
    arr[i][2] = bb
    arr[i][3] = cc
cnt = 0


def car_r():
    global start_r, start_c
    r, c = start_r, start_c
    r_c = -1
    for i in range(1, r + 1):
        # 해당 열 쫙 뽑음
        data = arr[i][1:c + 1]
        # 각 값에 대한 빈도값 체크
        dict = {data[j]: data.count(data[j]) for j in range(len(data))}
        if 0 in dict.keys():
            dict.pop(0)
        tp = list(dict.items())
        # (수와 등장 횟수)
        tp.sort(key=lambda x: (x[1], x[0]))

        if len(tp) > 50:
            l = 50
        else:
            l = len(tp)

        r_c = max(r_c, l * 2)
        temp = []
        for t in range(l):
            a, b = tp[t]
            temp.append(a)
            temp.append(b)
        arr[i][1:l * 2] = temp
        for t in range(l * 2 + 1, 101):
            arr[i][t] = 0
    start_c = r_c


def car_c():
    global start_r, start_c
    r, c = start_r, start_c
    r_c = -1
    for i in range(1, c + 1):
        data = []
        for j in range(1, r + 1):
            data.append(arr[j][i])
        # 각 값에 대한 빈도값 체크
        dict = {data[j]: data.count(data[j]) for j in range(len(data))}
        if 0 in dict.keys():
            dict.pop(0)
        tp = list(dict.items())
        # (수와 등장 횟수)
        tp.sort(key=lambda x: (x[1], x[0]))

        if len(tp) > 50:
            l = 50
        else:
            l = len(tp)

        r_c = max(r_c, l * 2)
        temp = []
        for t in range(l):
            a, b = tp[t]
            temp.append(a)
            temp.append(b)
        for t in range(len(temp)):
            arr[t + 1][i] = temp[t]
        for t in range(l * 2 + 1, 101):
            arr[t][i] = 0
    start_r = r_c


while True:
    if cnt > 100:
        print(-1)
        break
    if arr[r][c] == k:
        print(cnt)
        break
    if start_r >= start_c:
        car_r()
        cnt += 1
    else:
        car_c()
        cnt += 1
