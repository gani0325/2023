# codetree 참고함
# 바이러스 실험
# n * n 격자 무늬의 배지에 바이러스를 배양하는 실험
# 초기에 각 칸에 5만큼의 양분이 들어있으며 m개의 바이러스로 시작

# 한 사이클마다 실험 규칙
# 1. 각각의 바이러스는 본인이 속한 1 * 1 크기의 칸에 있는 양분을 섭취
# 본인의 나이만큼 양분을 섭취하며, 같은 칸에 여러 개의 바이러스가 있을 때에는 나이가 어린 바이러스부터 양분을 섭취
# 양분을 섭취한 바이러스는 나이가 1 증가
# 만약 양분이 부족하여 본인의 나이만큼 양분을 섭취할 수 없다면 그 즉시 죽는다
# 2. 모든 바이러스가 섭취를 끝낸 후 죽은 바이러스가 양분으로 변함
# 죽은 바이러스마다 나이를 2로 나눈 값이 바이러스가 있던 칸에 양분으로 추가 (소숫점 아래는 버림)
# 3. 바이러스가 번식을 진행
# 번식은 5의 배수의 나이를 가진 바이러스에게만 진행되며, 인접한 8개의 칸에 나이가 1인 바이러스가 생김
# 상하좌우와 대각선으로 인접한 8칸을 뜻하고, 배지 범위를 벗어난 곳에는 바이러스가 번식하지 않음
# 4. 1, 2, 3 과정이 순서대로 끝난 뒤에는 주어진 양분의 양에 따라 칸에 양분이 추가

# k 사이클이 끝난 이후에도 살아있는 바이러스의 양을 출력하는 프로그램

# 첫번째 줄에는 배지의 크기 n, 바이러스의 개수 m, 총 사이클의 수 k
# 두번째 줄부터 n+1번째 줄까지는 마지막에 추가되는 양분의 양
# 그 다음 줄부터 m개의 줄에는 바이러스의 정보
# 바이러스의 위치 : r은 격자의 몇번째 행, c는 격자의 몇번째 열, 세번째 정수로는 바이러스의 나이

# 배지의 크기 n, 바이러스의 개수 m, 총 사이클의 수 k
n, m, k = map(int, input().split())

virus = [[[] for _ in range(n)] for _ in range(n)]
next_virus = [[[] for _ in range(n)] for _ in range(n)]
food = [[0 for _ in range(n)]for _ in range(n)]
next_food = [[0 for _ in range(n)] for _ in range(n)]
delta = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# (x, y)를 기준으로 8방향으로 번식을 진행
def breed(x, y):
    dxs = [-1, -1, -1,  0, 0,  1, 1, 1]
    dys = [-1,  0,  1, -1, 1, -1, 0, 1]
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        # 격자 안이라면 나이가 1인 바이러스를 추가
        if in_range(nx, ny):
            next_virus[nx][ny].append(1)

def simulate():
    # 그 다음 바이러스, 양분 값을 초기화
    for i in range(n):
        for j in range(n):
            next_virus[i][j] = []
            next_food[i][j] = 0

        
    # Step1. 바이러스가 양분을 섭취
    for i in range(n):
        for j in range(n):
            # Step1-1. 바이러스를 나이순으로 정렬
            virus[i][j].sort()
            
            # Step1-2. 어린 바이러스부터 순서대로 양분을 섭취
            for age in virus[i][j]:
                # Case1.
                # 양분이 충분하다면 바이러스는 나이가 1 증가
                if food[i][j] >= age:
                    food[i][j] -= age
                    next_virus[i][j].append(age + 1)
                
                # Case2.
                # 양분이 불충분하다면 바이러스는 죽고 양분으로 쓰임
                else:
                    next_food[i][j] += age // 2
            
            # Step1-3. 남은 양분 만큼을 그 다음 양분으로 넣어줌
            next_food[i][j] += food[i][j]

    # Step2. 바이러스가 번식을 진행
    for i in range(n):
        for j in range(n):
            for age in next_virus[i][j]:
                if age % 5 == 0:
                    breed(i, j)
    
    # Step3. 각 칸에 입력으로 주어진 만큼 양분이 추가
    for i in range(n):
        for j in range(n):
            next_food[i][j] += delta[i][j]
    
    # 바이러스, 양분 값을 갱신
    for i in range(n):
        for j in range(n):
            virus[i][j] = next_virus[i][j][:]
            food[i][j] = next_food[i][j]

for _ in range(m):
    # 바이러스의 위치 (r은 격자의 몇번째 행, c는 격자의 몇번째 열), age는 바이러스의 나이
    r, c, age = map(int, input().split())
    virus[r - 1][c - 1].append(age)

# 초기 양분 값
for i in range(n):
    for j in range(n):
        food[i][j] = 5
        
# 총 k번 시뮬레이션을 진행
for _ in range(k):
    simulate()

ans = sum([
    len(virus[i][j])
    for i in range(n)
    for j in range(n)
])
print(ans)

##################예제######################
"""
입력:
5 3 2
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
2 2 2
3 4 3
4 5 4

출력:
6
"""