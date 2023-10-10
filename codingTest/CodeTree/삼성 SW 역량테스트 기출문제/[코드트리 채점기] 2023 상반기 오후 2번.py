"""
💛 코드트리 채점기
코드트리에 코드 제출이 올라오면 이를 어떻게 처리하는지에 대한 정보는 아래와 같습니다.

(1) 코드트리 채점기 준비
N개의 채점기가 준비되어 있고, 초기 문제 url에 해당하는 u0 ​가 주어집니다.
문제에서의 url은 도메인/문제ID 형태로 주어집니다.
도메인은 알파벳 소문자와 '.'으로만 이루어져 있고, 문제 ID는 1이상 10억 이하의 정수값으로 이루어져 있습니다.
N개의 채점기에는 1번부터 N번까지 번호가 붙어있고, 0초에 채점 우선순위가 1이면서 url이 u0​ 인 초기 문제에 대한 채점 요청이 들어오게 됩니다. 
채점 task는 채점 대기 큐에 들어가게 됩니다.

(2) 채점 요청
t초에 채점 우선순위가 p이면서 url이 u인 문제에 대한 채점 요청이 들어오게 됩니다. 
채점 task는 채점 대기 큐에 들어가게 됩니다. 
단, 채점 대기 큐에 있는 task 중 정확히 u와 일치하는 url이 단 하나라도 존재한다면 큐에 추가하지 않고 넘어갑니다.

(3) 채점 시도
t초에 채점 대기 큐에서 즉시 채점이 가능한 경우 중 우선순위가 가장 높은 채점 task를 골라 채점을 진행합니다.
우선 어떠한 task가 채점이 될 수 없는 조건은 다음과 같습니다.
    해당 task의 도메인이 현재 채점을 진행중인 도메인 중 하나라면 불가능합니다.
    해당 task의 도메인과 정확히 일치하는 도메인에 대해 가장 최근에 진행된 채점 시작 시간이 start, 종료 시간이 start+gap
        현재 시간 t가 start+3×gap 보다 작다면, 부적절한 채점이라 의심되기에 채점이 불가합니다.

즉시 채점이 가능한 경우 중 우선순위가 가장 높은 채점 task는 아래 조건에 따라 골라집니다.
    채점 우선순위 p의 번호가작을수록 우선순위가 높습니다.
    만약 채점 우선순위가 동일하다면 채점 task가 채점 대기 큐에 들어온 시간이 더 빠를수록 우선순위가 높습니다.
t초에 채점이 가능한 task가 단 하나라도 있었다면, 
쉬고 있는 채점기 중 가장 번호가 작은 채점기가 우선순위가 가장 높은 채점 task에 대한 채점을 시작합니다. 만약 쉬고 있는 채점기가 없다면 요청을 무시하고 넘어갑니다.

(4) 채점 종료
t초에 J id 번 채점기가 진행하던 채점이 종료됩니다. J id  채점기는 다시 쉬는 상태가 됩니다.
만약 J id 번 채점기가 진행하던 채점이 없었다면 이 명령은 무시됩니다.

(5) 채점 대기 큐 조회
시간 t에 채점 대기 큐에 있는 채점 task의 수를 출력합니다.
Q번에 걸쳐 명령을 순서대로 진행하며 알맞은 답을 출력하는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 명령의 수 Q가 주어집니다.
두 번째 줄부터는 Q개의 줄에 걸쳐 명령의 정보가 주어집니다. 각 명령에 따른 형태는 다음과 같습니다.
    코드트리 채점기 준비
        100 N u0 형태로 공백을 사이에 두고 주어집니다. 이는 N개의 채점기가 있으며 초기 문제 url이 u0 임을 뜻합니다.
        이 명령은 항상 첫 번째 명령으로만 주어지며, 항상 주어집니다.
    채점 요청
        200 t p u 형태로 공백을 사이에 두고 주어집니다. 
        이는 t초에 채점 우선순위가 p이며 url이 u인 문제에 대한 채점 요청이 들어왔음을 의미합니다.
    채점 시도
        300 t 형태로 공백을 사이에 두고 주어집니다. 
        이는 t초에 채점 대기 큐에서 즉시 채점이 가능한 경우 중 우선순위가 가장 높은 채점 task를 골라 채점을 진행하게 됨을 뜻합니다.
    채점 종료
        400 t J_id 형태로 공백을 사이에 두고 주어집니다. 이는 t초에 J id​ 번 채점기가 진행하던 채점이 종료됨을 뜻합니다.
    채점 대기 큐 조회
        500 t 형태로 공백을 사이에 두고 주어집니다. 이 경우 시간 t에 채점 대기 큐에 있는 채점 task의 수를 출력해야합니다.

1 ≤ Q ≤ 50,000
1 ≤ N ≤ 50,000
1 ≤ 도메인의 길이 ≤ 19
1 ≤ 주어지는 서로 다른 도메인의 수 ≤ 300
1 ≤ 문제 ID ≤ 1,000,000,000
1 ≤ p ≤ N
1 ≤ J id  ≤ N
1 ≤ t ≤ 1,000,000
입력으로 주어지는 t 값은 모두 다르며, 오름차순으로 정렬되어 주어짐을 가정해도 좋습니다.

💚 출력 형식
500명령어에 대해 채점 대기 큐에 있는 task의 수를 한 줄에 하나씩 출력합니다.

🐧 입출력 예제
예제1
➡️ 입력:
19
100 3 codetree.ai/16
300 1
400 4 1
200 5 1 codetree.ai/17
200 6 1 codetree.ai/17
500 7
300 8
500 9
300 11
400 12 1
500 13
200 14 3 codetree.ai/18
200 15 2 codetree.ai/20
200 16 2 tree.ai/1
500 17
300 18
500 19
200 20 1 codetree.ai/20
500 21

➡️ 출력:
1 
1
0
3
2
3
"""
from sortedcontainers import SortedSet, SortedDict
import heapq
import sys


class PriorityQueue:
    def __init__(self):          # 빈 Priority Queue 하나를 생성합니다.
        self.items = []

    def push(self, item):        # 우선순위 큐에 데이터를 추가합니다.
        heapq.heappush(self.items, item)

    def empty(self):             # 우선순위 큐가 비어있으면 True를 반환합니다.
        return not self.items

    def size(self):              # 우선순위 큐에 있는 데이터 수를 반환합니다.
        return len(self.items)

    def pop(self):               # 우선순위 큐에 있는 데이터 중 최솟값에 해당하는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")

        return heapq.heappop(self.items)

    # 우선순위 큐에 있는 데이터 중 최솟값에 해당하는 데이터를 제거하지 않고 반환합니다.
    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")

        return self.items[0]


MAX_D = 300
MAX_N = 50000
INF = sys.maxsize

# 해당 도메인에서 해당 문제ID가 레디큐에 있는지 관리해줍니다.
is_in_readyq = [SortedSet() for _ in range(MAX_D + 1)]

# 현재 쉬고 있는 채점기들을 관리해줍니다.
rest_judger = PriorityQueue()

# 각 채점기들이 채점할 때, 도메인의 인덱스를 저장합니다.
judging_domain = [0 for _ in range(MAX_N + 1)]

# 각 도메인별 start, gap, end(채점이 가능한 최소 시간)을 관리합니다.
s = [0 for _ in range(MAX_D + 1)]
g = [0 for _ in range(MAX_D + 1)]
e = [0 for _ in range(MAX_D + 1)]

# 도메인을 관리하기 위해 cnt를 이용합니다.
# 도메인 문자열을 int로 변환해주는 map을 관리합니다.
domainToIdx = SortedDict()
global cnt
cnt = 0

# 현재 채점 대기 큐에 있는 task의 개수를 관리합니다.
global ans
ans = 0

# 각 도메인별로 priority queue를 만들어
# 우선순위가 가장 높은 url을 뽑아줍니다.
url_pq = [PriorityQueue() for _ in range(MAX_D + 1)]


# 채점기를 준비합니다.
def Init(query):
    global n
    (empty, n, url) = query
    n = int(n)

    global cnt

    for i in range(1, n + 1):
        rest_judger.push(i)

    # url에서 도메인 부분과 숫자 부분을 나누어줍니다.
    idx = 0
    for i in range(len(url)):
        if url[i] == '/':
            idx = i

    domain = url[:idx]
    num = int(url[idx + 1:])

    # 만약 도메인이 처음 나온 도메인이라면 domainToIdx에 갱신합니다.
    if not domain in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
    domain_idx = domainToIdx[domain]

    # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣어줍니다.
    is_in_readyq[domain_idx].add(num)

    # 새로 들어온 url을 도메인에 맞춰 url_pq에 넣어줍니다.
    # id, tme, num
    newUrl = (1, 0, num)
    url_pq[domain_idx].push(newUrl)

    # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가합니다.
    global ans
    ans += 1


# 새로운 url을 입력받아 레디큐에 추가해줍니다.
def NewUrl(query):
    (empty, tme, id, url) = query
    tme = int(tme)
    id = int(id)

    global cnt

    # url에서 도메인 부분과 숫자 부분을 나누어줍니다.
    idx = 0
    for i in range(len(url)):
        if url[i] == '/':
            idx = i

    domain = url[:idx]
    num = int(url[idx + 1:])

    # 만약 도메인이 처음 나온 도메인이라면 domainToIdx에 갱신합니다.
    if domain not in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt

    domain_idx = domainToIdx[domain]

    # 만약 숫자 부분이 이미 레디큐에 있으면 중복되므로 넘어갑니다.
    if num in is_in_readyq[domain_idx]:
        return
    # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣어줍니다.
    is_in_readyq[domain_idx].add(num)

    # 새로 들어온 url을 도메인에 맞춰 url_pq에 넣어줍니다.
    # id, tme, num
    newUrl = (id, tme, num)
    url_pq[domain_idx].push(newUrl)

    # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가합니다.
    global ans
    ans += 1


# 다음 도메인을 찾아 assign합니다.
def Assign(query):
    (empty, tme) = query
    tme = int(tme)

    # 쉬고 있는 채점기가 없다면 넘어갑니다.
    if rest_judger.empty():
        return

    # 가장 우선순위가 높은 url을 찾습니다.
    min_domain = 0
    minUrl = (INF, 0, 0)

    global cnt

    for i in range(1, cnt + 1):
        # 만약 현재 채점중이거나, 현재 시간에 이용할 수 없다면 넘어갑니다.
        if e[i] > tme:
            continue

        # 만약 i번 도메인에 해당하는 url이 존재한다면
        # 해당 도메인에서 가장 우선순위가 높은 url을 뽑고 갱신해줍니다.
        if not url_pq[i].empty():
            curUrl = url_pq[i].top()

            if minUrl > curUrl:
                minUrl = curUrl
                min_domain = i

    # 만약 가장 우선순위가 높은 url이 존재하면
    # 해당 도메인과 쉬고 있는 가장 낮은 번호의 채점기를 연결해줍니다.
    if min_domain:
        judger_idx = rest_judger.top()
        rest_judger.pop()

        # 해당 도메인의 가장 우선순위가 높은 url을 지웁니다.
        url_pq[min_domain].pop()

        # 도메인의 start, end를 갱신해줍니다.
        s[min_domain] = tme
        e[min_domain] = INF

        # judger_idx번 채점기가 채점하고 있는 도메인 번호를 갱신해줍니다.
        judging_domain[judger_idx] = min_domain

        # 레디큐에서 해당 url의 숫자를 지워줍니다.
        is_in_readyq[min_domain].remove(minUrl[2])

        # 채점 대기 큐에 값이 지워졌으므로 개수를 1 감소합니다.
        global ans
        ans -= 1


# 채점 하나를 마무리합니다.
def Finish(query):
    (empty, tme, id) = query
    tme = int(tme)
    id = int(id)

    # 만약 id번 채점기가 채점 중이 아닐 경우 스킵합니다.
    if judging_domain[id] == 0:
        return

    # id번 채점기를 마무리합니다.
    rest_judger.push(id)
    domain_idx = judging_domain[id]
    judging_domain[id] = 0

    # 해당 도메인의 gap, end 값을 갱신해줍니다.
    g[domain_idx] = tme - s[domain_idx]
    e[domain_idx] = s[domain_idx] + 3 * g[domain_idx]


# 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
def Check(query):
    (empty, tme) = query
    tme = int(tme)

    global ans
    print(ans)


q = int(input())

for _ in range(q):
    query = input().split()

    if int(query[0]) == 100:
        # 채점기를 준비합니다.
        Init(query)
    if int(query[0]) == 200:
        # 새로운 url을 입력받아 레디큐에 추가해줍니다.
        NewUrl(query)
    if int(query[0]) == 300:
        # 다음 도메인을 찾아 assign합니다.
        Assign(query)
    if int(query[0]) == 400:
        # 채점 하나를 마무리합니다.
        Finish(query)
    if int(query[0]) == 500:
        # 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
        Check(query)
