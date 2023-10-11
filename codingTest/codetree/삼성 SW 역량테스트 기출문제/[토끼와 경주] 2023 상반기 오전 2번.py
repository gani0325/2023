"""
💛 토끼와 경주
토끼들이 점수를 건 경주를 진행하려고 합니다. 경주에 관한 정보는 아래와 같습니다.

(1) 경주 시작 준비
P 마리의 토끼가 N×M 크기의 격자 위에서 경주를 진행할 준비를 합니다. 
각 토끼에게는 고유한 번호가 붙어있으며, 한번 움직일 시 꼭 이동해야 하는 거리도 정해져 있습니다. 
i번 토끼의 고유번호는 pid i, 이동해야 하는 거리는 d i  입니다. 처음 토끼들은 전부 (1행, 1열)에 있습니다.

(2) 경주 진행
가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 K번 반복합니다.
우선순위는 순서대로 (현재까지의 총 점프 횟수가 적은 토끼, 현재 서있는 행 번호 + 열 번호가 작은 토끼, 행 번호가 작은 토끼, 
열 번호가 작은 토끼, 고유번호가 작은 토끼) 순입니다. 

첫 번째 우선순위가 높은 토끼가 한마리 뿐이라면 바로 결정되는 것이고, 동률이라면 두 번째 우선순위를 보고, .. 
이러한 규칙에 의해 가장 우선순위가 높은 토끼가 결정됩니다.


우선순위가 가장 높은 토끼가 결정이 되면 이 토끼를 i번 토끼라 했을 때 상하좌우 네 방향으로 각각 d i​ 만큼 이동했을 때의 위치를 구합니다. 
이때 이동하는 도중 그 다음 칸이 격자를 벗어나게 된다면 방향을 반대로 바꿔 한 칸 이동하게 됩니다. 
이렇게 구해진 4개의 위치 중 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순으로 우선순위를 두었을 때 
가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼를 이동시킵니다.

이 칸의 위치를 (r i ,c i )라 했을 때 i번 토끼를 제외한 나머지 P−1마리의 토끼들은 전부 r i +c i 만큼의 점수를 동시에 얻게 됩니다.
이렇게 K번의 턴 동안 가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 반복하게 되며, 이 과정에서 동일한 토끼가 여러번 선택되는 것 역시 가능합니다.

K번의 턴이 모두 진행된 직후에는 (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼) 순으로 우선순위를 두었을 때 
가장 우선순위가 높은 토끼를 골라 점수 S를 더해주게 됩니다. 
단, 이 경우에는 K번의 턴 동안 한번이라도 뽑혔던 적이 있던 토끼 중 가장 우선순위가 높은 토끼를 골라야만 함에 꼭 유의합니다.

(3) 이동거리 변경
고유번호가 pid t​ 인 토끼의 이동거리를 L배 해줍니다. 단, 계산 도중 특정 토끼의 이동거리가 10억을 넘어가는 일은 발생하지 않음을 가정해도 좋습니다.

(4) 최고의 토끼 선정
각 토끼가 모든 경주를 진행하며 얻은 점수 중 가장 높은 점수를 출력합니다.

Q번에 걸쳐 명령을 순서대로 진행하며 최고의 토끼를 선정해주는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 명령의 수 Q가 주어집니다.
두 번째 줄부터는 Q개의 줄에 걸쳐 명령의 정보가 주어집니다. 각 명령에 따른 형태는 다음과 같습니다.
    경주 시작 준비
        100 N M P pid_1 d_1 pid_2 d_2 ... pid_p d_p 형태로 공백을 사이에 두고 주어집니다. 
        이는 P 마리의 토끼가 N×M 크기의 격자 위에서 경주를 진행하며 i번 토끼의 고유 번호는 pid i, 이동해야 하는 거리가 d i임을 뜻합니다. 
        이 명령은 항상 첫 번째 명령으로만 주어지며, 항상 주어집니다. 또한, 이 명령에 대해서는 출력할 값이 없습니다.

    경주 진행
        200 K S 형태로 공백을 사이에 두고 주어집니다. 이 명령은 최대 2000번까지만 주어집니다.
    이동거리 변경
        300 pid_t L 형태로 공백을 사이에 두고 주어집니다. 이 명령은 최대 2000번까지만 주어집니다.
    최고의 토끼 선정
        400 형태로 주어집니다. 이 명령어는 정확히 마지막 명령으로만 주어지며, 항상 주어집니다.
    2 ≤ Q ≤ 4,002
    2 ≤ N,M ≤ 100,000
    1 ≤ P ≤ 2,000
    1 ≤ pid i, pid t ≤ 10,000,000
    1 ≤ d i ≤ 1,000,000,000
    1 ≤ K ≤ min(100,P)
    1 ≤ S ≤ 1,000,000
    1 ≤ L ≤ 1,000,000,000

💚 출력 형식
400명령어에 대해 P마리의 토끼의 최종 점수 중 최댓값을 출력합니다. 
400 명령어는 맨 끝에 단 한번만 주어지기에, 답은 첫 번째 줄에만 출력하면 됩니다.

🐧 입출력 예제
예제1
➡️ 입력:
5
100 3 5 2 10 2 20 5
200 6 100
300 10 2
200 3 20
400

➡️ 출력:
151
"""

import heapq

MAX_N = 2000

# 변수 선언 및 입력:
n, m, p = 0, 0, 0

# 각 토끼의 id를 기록해줍니다.
pid = [0] * (MAX_N + 1)

# 각 토끼의 이동거리를 기록해줍니다.
pw = [0] * (MAX_N + 1)

# 각 토끼의 점프 횟수를 기록해줍니다.
jump_cnt = [0] * (MAX_N + 1)

# 각 토끼의 점수를 기록해줍니다.
result = [0] * (MAX_N + 1)

# 각 토끼의 현재 위치(좌표)를 기록해줍니다.
point = [(0, 0)] * (MAX_N + 1)

# 각 토끼의 id를 인덱스 번호로 변환해줍니다.
id_to_idx = {}

# 각각의 경주에서 토끼가 달렸는지 여부를 기록해줍니다.
is_runned = [0] * (MAX_N + 1)

# 하나를 제외한 모든 토끼의 점수를 더하는 쿼리를 편하게 하기 위해
# total_sum이라는 변수를 추가해줍니다.
total_sum = 0


# 구조체 rabbit을 정리해 관리합니다.
class Rabbit:
    def __init__(self, x, y, j, pid):
        self.x = x
        self.y = y
        self.j = j
        self.pid = pid

    # 이동할 토끼를 결정하기 위해 정렬함수를 만들어줍니다.
    def __lt__(self, other):
        if self.j != other.j:
            return self.j < other.j
        if self.x + self.y != other.x + other.y:
            return self.x + self.y < other.x + other.y
        if self.x != other.x:
            return self.x < other.x
        if self.y != other.y:
            return self.y < other.y
        return self.pid < other.pid


# 가장 긴 위치를 판단하기 위해 정렬함수를 하나 더 만들어줍니다.
def compare(a, b):
    if a.x + a.y != b.x + b.y:
        return a.x + a.y < b.x + b.y
    if a.x != b.x:
        return a.x < b.x
    if a.y != b.y:
        return a.y < b.y
    return a.pid < b.pid


# 경주 시작 준비 쿼리를 처리해줍니다.
def init(inp):
    global n, m, p

    n, m, p, *rabbits = inp
    for i in range(1, p + 1):
        pid[i] = rabbits[i * 2 - 2]
        pw[i] = rabbits[i * 2 - 1]

        id_to_idx[pid[i]] = i
        point[i] = (1, 1)


# 토끼를 위로 이동시킵니다.
def get_up_rabbit(cur_rabbit, dis):
    up_rabbit = cur_rabbit
    dis %= 2 * (n - 1)

    if dis >= up_rabbit.x - 1:
        dis -= (up_rabbit.x - 1)
        up_rabbit.x = 1
    else:
        up_rabbit.x -= dis
        dis = 0

    if dis >= n - up_rabbit.x:
        dis -= (n - up_rabbit.x)
        up_rabbit.x = n
    else:
        up_rabbit.x += dis
        dis = 0

    up_rabbit.x -= dis

    return up_rabbit


# 토끼를 아래로 이동시킵니다.
def get_down_rabbit(cur_rabbit, dis):
    down_rabbit = cur_rabbit
    dis %= 2 * (n - 1)

    if dis >= n - down_rabbit.x:
        dis -= (n - down_rabbit.x)
        down_rabbit.x = n
    else:
        down_rabbit.x += dis
        dis = 0

    if dis >= down_rabbit.x - 1:
        dis -= (down_rabbit.x - 1)
        down_rabbit.x = 1
    else:
        down_rabbit.x -= dis
        dis = 0

    down_rabbit.x += dis

    return down_rabbit


# 토끼를 왼쪽으로 이동시킵니다.
def get_left_rabbit(cur_rabbit, dis):
    left_rabbit = cur_rabbit
    dis %= 2 * (m - 1)

    if dis >= left_rabbit.y - 1:
        dis -= (left_rabbit.y - 1)
        left_rabbit.y = 1
    else:
        left_rabbit.y -= dis
        dis = 0

    if dis >= m - left_rabbit.y:
        dis -= (m - left_rabbit.y)
        left_rabbit.y = m
    else:
        left_rabbit.y += dis
        dis = 0

    left_rabbit.y -= dis

    return left_rabbit


# 토끼를 오른쪽으로 이동시킵니다.
def get_right_rabbit(cur_rabbit, dis):
    right_rabbit = cur_rabbit
    dis %= 2 * (m - 1)

    if dis >= m - right_rabbit.y:
        dis -= (m - right_rabbit.y)
        right_rabbit.y = m
    else:
        right_rabbit.y += dis
        dis = 0

    if dis >= right_rabbit.y - 1:
        dis -= (right_rabbit.y - 1)
        right_rabbit.y = 1
    else:
        right_rabbit.y -= dis
        dis = 0

    right_rabbit.y += dis

    return right_rabbit


def copy_rabbit(rabbit):
    return Rabbit(rabbit.x, rabbit.y, rabbit.j, rabbit.pid)


# 경주를 진행합니다.
def start_round(inp):
    global total_sum

    k, bonus = inp
    rabbit_pq = []

    for i in range(1, p + 1):
        is_runned[i] = False

    # 우선 p마리의 토끼들을 전부 priority queue에 넣어줍니다.
    for i in range(1, p + 1):
        x, y = point[i]
        new_rabbit = Rabbit(x, y, jump_cnt[i], pid[i])
        heapq.heappush(rabbit_pq, new_rabbit)

    # 경주를 k회 진행합니다.
    for _ in range(k):
        # 우선순위가 가장 높은 토끼를 priority queue에서 뽑아옵니다.
        cur_rabbit = heapq.heappop(rabbit_pq)

        # 해당 토끼를 상, 하, 좌, 우 4개의 방향으로 이동시킵니다.
        # 각각의 방향으로 이동시킨 후 최종 위치를 구하고
        # 가장 시작점으로부터 멀리 있는 위치를 찾아줍니다.
        dis = pw[id_to_idx[cur_rabbit.pid]]
        nex_rabbit = copy_rabbit(cur_rabbit)
        nex_rabbit.x = 0
        nex_rabbit.y = 0

        # 토끼를 위로 이동시킵니다.
        up_rabbit = get_up_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, up_rabbit):
            nex_rabbit = up_rabbit

        # 토끼를 아래로 이동시킵니다.
        down_rabbit = get_down_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, down_rabbit):
            nex_rabbit = down_rabbit

        # 토끼를 왼쪽으로 이동시킵니다.
        left_rabbit = get_left_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, left_rabbit):
            nex_rabbit = left_rabbit

        # 토끼를 오른쪽으로 이동시킵니다.
        right_rabbit = get_right_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지를 갱신합니다.
        if compare(nex_rabbit, right_rabbit):
            nex_rabbit = right_rabbit

        # 토끼의 점프 횟수를 갱신해주고, priority queue에 다시 집어넣습니다.
        nex_rabbit.j += 1
        heapq.heappush(rabbit_pq, nex_rabbit)

        # 실제 point, jump_cnt 배열에도 값을 갱신해줍니다.
        nex_idx = id_to_idx[nex_rabbit.pid]
        point[nex_idx] = (nex_rabbit.x, nex_rabbit.y)
        jump_cnt[nex_idx] += 1

        # 토끼가 달렸는지 여부를 체크해줍니다.
        is_runned[nex_idx] = True

        # 토끼가 받는 점수는 (현재 뛴 토끼)만 (r + c)만큼 점수를 빼주고,
        # 모든 토끼(total_sum)에게 (r + c)만큼 점수를 더해줍니다.
        # 최종적으로 i번 토끼가 받는 점수는 result[i] + total_sum이 됩니다.
        result[nex_idx] -= (nex_rabbit.x + nex_rabbit.y)
        total_sum += (nex_rabbit.x + nex_rabbit.y)

    # 보너스 점수를 받을 토끼를 찾습니다.
    # 이번 경주때 달린 토끼 중 가장 멀리있는 토끼를 찾습니다.
    bonus_rabbit = Rabbit(0, 0, 0, 0)
    while rabbit_pq:
        cur_rabbit = heapq.heappop(rabbit_pq)

        # 달리지 않은 토끼는 스킵합니다.
        if not is_runned[id_to_idx[cur_rabbit.pid]]:
            continue

        if compare(bonus_rabbit, cur_rabbit):
            bonus_rabbit = cur_rabbit

    # 해당 토끼에게 bonus만큼 점수를 추가해줍니다.
    result[id_to_idx[bonus_rabbit.pid]] += bonus


# 이동거리를 변경합니다.
def power_up(inp):
    pid, t = inp
    idx = id_to_idx[pid]

    pw[idx] *= t


# 최고의 토끼를 선정합니다.
def print_result():
    ans = 0
    for i in range(1, p + 1):
        ans = max(ans, result[i] + total_sum)

    print(ans)


q = int(input())
for _ in range(q):
    query, *inp = list(map(int, input().split()))

    # 경주 시작 준비 쿼리를 처리해줍니다.
    if query == 100:
        init(inp)
    # 경주를 진행합니다.
    if query == 200:
        start_round(inp)
    # 이동거리를 변경합니다.
    if query == 300:
        power_up(inp)
    # 최고의 토끼를 선정합니다.
    if query == 400:
        print_result()
