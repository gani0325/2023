"""
💛 산타의 선물 공장 2
급할 때 선물 공장을 세웠던 산타는 이제 각 벨트의 정보와 선물의 정보를 조회할 수 있는 기능들을 추가하여 새로운 공장을 만들고자 합니다.

1. 공장 설립
선물 공장에 n개의 벨트를 설치하고, 총 m개의 물건을 준비합니다. 
m개의 선물의 위치가 공백을 사이에 두고 주어집니다. <Figure 1>은 n이 4이고 m이 6인 한 가지 예입니다. 
각각 선물의 번호는 오름차순으로 벨트에 쌓입니다.

2. 물건 모두 옮기기
m_src번째 벨트에 있는 선물들을 모두 m_dst번째 벨트의 선물들로 옮깁니다. 
옯겨진 선물들은 m_dst 벨트 앞에 위치합니다. 만약 m_src번째 벨트에 선물이 존재하지 않다면 아무것도 옮기지 않아도 됩니다. 
옮긴 뒤에 m_dst번째 벨트에 있는 선물들의 개수를 출력합니다.
예로 <Figure 1>에서 2번째에서 4번째로 옮기게 된다면 <Figure 2>처럼 변하게 됩니다. 4번째 벨트의 총 선물 개수인 4를 출력합니다.

3. 앞 물건만 교체하기
m_src번째 벨트에 있는 선물 중 가장 앞에 있는 선물을 m_dst번째 벨트의 선물들 중 가장 앞에 있는 선물과 교체합니다. 
둘 중 하나의 벨트에 선물이 아예 존재하지 않다면 교체하지 않고 해당 벨트로 선물을 옮기기만 합니다. 
옮긴 뒤에 m_dst번째 벨트에 있는 선물들의 개수를 출력합니다.
예로 <Figure 2>에서 2번째 벨트와 4번째 벨트의 앞 물건만 교체하게 되면 다음과 같이 바뀌고, 3을 출력하게 됩니다.

4. 물건 나누기
m_src번째 벨트에 있는 선물들의 개수를 n이라고 할 때 가장 앞에서 floor(n/2)번째까지 있는 선물을 m_dst번째 벨트 앞으로 옮깁니다. 
만약 m_src 벨트에 선물이 1개인 경우에는 선물을 옮기지 않습니다. 옮긴 뒤에 m_dst번째 벨트에 있는 선물들의 개수를 출력합니다.
예로 <Figure 3>에서 4번 벨트에서 2번 벨트로 옮기게 되면 다음과 같이 옮겨지고, 2를 출력하게 됩니다.

5. 선물 정보 얻기
선물 번호 p_num가 주어질 때, 해당 선물의 앞 선물의 번호 a과 뒤 선물의 번호 b라 할 때 a + 2 * b를 출력합니다. 
만약 앞 선물이 없는 경우에는 a = -1, 뒤 선물이 없는 경우에는 b = -1을 넣어줍니다.
예로 <Figure 4>에서 p_num이 6인 선물 정보를 구하는 경우에는 2을 출력(4 + -1 * 2)하고, 
p_num이 5인 선물 정보를 구하는 경우에는 -1이 출력(1 + -1 * 2)되게 됩니다.

6. 벨트 정보 얻기
벨트 번호 b_num이 주어질 때, 해당 벨트의 맨 앞에 있는 선물의 번호를 a, 맨 뒤에 있는 선물의 번호를 b, 
해당 벨트에 있는 선물의 개수를 c라고 할 때, a + 2*b + 3*c의 값을 출력합니다. 
선물이 없는 벨트의 경우에는 a와 b 모두 -1이 됩니다.
예로 <Figure 4>에서 b_num이 1인 벨트의 정보를 구하면 17(1 + 2 * 5 + 3 * 2)을 출력합니다. 
b_num이 3인 벨트의 정보를 구하면 -3(-1 + -1 * 2 + 0)이 됩니다.

산타가 q번에 걸쳐 명령을 순서대로 진행하며 원하는 결과를 출력하는 프로그램을 작성해보세요.

🧡 입력 형식
첫 번째 줄에 명령의 수 q가 주어집니다.
두 번째 줄부터는 q개의 줄에 걸쳐 명령의 정보가 주어집니다. 각 명령에 따른 형태는 다음과 같습니다.

    공장 설립
    100 n m B_NUM1 B_NUM2 ... B_NUMm 형태로 공백을 사이에 두고 주어집니다. 
    이는 n개의 벨트와 m개의 선물로 이루어진 공장을 세우며, 선물을 주어진 벨트의 번호대로 1번 벨트부터 n번 벨트에 요청대로 올려줍니다. 
    이 명령은 항상 첫 번째 명령으로만 주어지며, 항상 주어집니다. 또한, 이 명령에 대해서는 출력할 값이 없습니다.

    물건 모두 옮기기
        200 m_src m_dst 형태로 공백을 사이에 두고 주어집니다. 이 명령에서는 진행 이후 m_dst의 선물의 총 수를 출력합니다. 
        m_src와 m_dst는 같지 않습니다.

    앞 물건만 교체하기
        300 m_src m_dst 형태로 공백을 사이에 두고 주어집니다. 이 명령에서는 진행 이후 m_dst의 선물의 총 수를 출력합니다. 
        m_src와 m_dst는 같지 않습니다.

    물건 나누기
        400 m_src m_dst 형태로 공백을 사이에 두고 주어집니다. 이 명령에서는 진행 이후 m_dst의 선물의 총 수를 출력합니다. 
        m_src와 m_dst는 같지 않습니다. 해당 명령은 최대 100번까지만 주어집니다.

    선물 정보 얻기
        500 p_num 형태로 공백을 사이에 두고 주어집니다. 앞 선물의 번호 a과 뒤 선물의 번호 b라 할 때 a + 2 * b를 출력합니다. 
        없을 경우에는 각각 -1을 대입합니다.

    벨트 정보 얻기
        600 b_num 형태로 공백을 사이에 두고 주어집니다. 해당 벨트의 맨 앞에 있는 선물의 번호를 a, 맨 뒤에 있는 선물의 번호를 b, 
        해당 벨트에 있는 선물의 개수를 c라고 할 때, a + 2*b + 3*c의 값을 출력합니다. 없을 경우에는 a, b에 각각 -1을 대입합니다. 
        이때의 c는 0이 됩니다.

    1 ≤ q ≤ 100,000
    2 ≤ n ≤ 100,000
    1 ≤ m ≤ 100,000
    1 ≤ p_num ≤ m
    1 ≤ b_num ≤ n

💚 출력 형식
산타가 q개의 명령을 진행하면서 출력해야 하는 값을 한 줄에 하나씩 출력합니다.

🐧 입출력 예제
예제1
➡️ 입력:
8
100 4 6 1 2 2 2 1 4
200 2 4
300 2 4
400 4 2
500 6
500 5
600 1
600 3

➡️ 출력:
4
3
2
2
-1
17
-3
"""
MAX_N = 100000
MAX_M = 100000

# 변수 선언
n, m, q = -1, -1, -1

# id에 해당하는 상자의 nxt값과 prv값을 관리합니다.
# 0이면 없다는 뜻입니다.
prv, nxt = [0] * (MAX_M + 1), [0] * (MAX_M + 1)

# 각 벨트별로 head, tail id, 그리고 총 선물 수를 관리합니다.
# 0이면 없다는 뜻입니다.
head, tail, num_gift = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N


# 공장 설립
def build_factory(elems):
    # 공장 정보를 입력받습니다.
    n, m = elems[1], elems[2]

    # 벨트 정보를 만들어줍니다.
    boxes = [[] for _ in range(n)]
    for _id in range(1, m + 1):
        b_num = elems[_id + 2]
        b_num -= 1

        boxes[b_num].append(_id)

    # 초기 벨트의 head, tail, nxt, prv값을 설정해줍니다.
    for i in range(n):
        # 비어있는 벨트라면 패스합니다.
        if len(boxes[i]) == 0:
            continue

        # head, tail을 설정해줍니다.
        head[i] = boxes[i][0]
        tail[i] = boxes[i][-1]

        # 벨트 내 선물 총 수를 관리해줍니다.
        num_gift[i] = len(boxes[i])

        # nxt, prv를 설정해줍니다.
        for j in range(len(boxes[i]) - 1):
            nxt[boxes[i][j]] = boxes[i][j + 1]
            prv[boxes[i][j + 1]] = boxes[i][j]


# 물건을 전부 옮겨줍니다.
def move(elems):
    m_src, m_dst = elems[1] - 1, elems[2] - 1

    # m_src에 물건이 없다면
    # 그대로 m_dst내 물건 수가 답이 됩니다.
    if num_gift[m_src] == 0:
        print(num_gift[m_dst])
        return

    # m_dst에 물건이 없다면
    # 그대로 옮겨줍니다.
    if num_gift[m_dst] == 0:
        head[m_dst] = head[m_src]
        tail[m_dst] = tail[m_src]
    else:
        orig_head = head[m_dst]
        # m_dst의 head를 교체해줍니다.
        head[m_dst] = head[m_src]
        # m_src의 tail과 기존 m_dst의 head를 연결해줍니다.
        src_tail = tail[m_src]
        nxt[src_tail] = orig_head
        prv[orig_head] = src_tail

    # head, tail을 비워줍니다.
    head[m_src] = tail[m_src] = 0

    # 선물 상자 수를 갱신해줍니다.
    num_gift[m_dst] += num_gift[m_src]
    num_gift[m_src] = 0

    print(num_gift[m_dst])


# 해당 벨트의 head를 제거합니다.
def remove_head(b_num):
    # 불가능하면 패스합니다.
    if not num_gift[b_num]:
        return 0

    # 노드가 1개라면
    # head, tail 전부 삭제 후
    # 반환합니다.
    if num_gift[b_num] == 1:
        _id = head[b_num]
        head[b_num] = tail[b_num] = 0
        num_gift[b_num] = 0
        return _id

    # head를 바꿔줍니다.
    hid = head[b_num]
    next_head = nxt[hid]
    nxt[hid] = prv[next_head] = 0
    num_gift[b_num] -= 1
    head[b_num] = next_head

    return hid


# 해당 밸트에 head를 추가합니다.
def push_head(b_num, hid):
    # 불가능한 경우는 진행하지 않습니다.
    if hid == 0:
        return

    # 비어있었다면
    # head, tail이 동시에 추가됩니다.
    if not num_gift[b_num]:
        head[b_num] = tail[b_num] = hid
        num_gift[b_num] = 1
    # 그렇지 않다면
    # head만 교체됩니다.
    else:
        orig_head = head[b_num]
        nxt[hid] = orig_head
        prv[orig_head] = hid
        head[b_num] = hid
        num_gift[b_num] += 1


# 앞 물건을 교체해줍니다.
def change(elems):
    m_src, m_dst = elems[1] - 1, elems[2] - 1

    src_head = remove_head(m_src)
    dst_head = remove_head(m_dst)
    push_head(m_dst, src_head)
    push_head(m_src, dst_head)

    print(num_gift[m_dst])


# 물건을 나눠옮겨줍니다.
def divide(elems):
    m_src, m_dst = elems[1] - 1, elems[2] - 1

    # 순서대로 src에서 박스들을 빼줍니다.
    cnt = num_gift[m_src]
    box_ids = []
    for _ in range(cnt // 2):
        box_ids.append(remove_head(m_src))

    # 거꾸로 뒤집어서 하나씩 dst에 박스들을 넣어줍니다.
    for i in range(len(box_ids) - 1, -1, -1):
        push_head(m_dst, box_ids[i])

    print(num_gift[m_dst])


# 선물 점수를 얻습니다.
def gift_score(elems):
    p_num = elems[1]

    a = prv[p_num] if prv[p_num] != 0 else -1
    b = nxt[p_num] if nxt[p_num] != 0 else -1

    print(a + 2 * b)


# 벨트 정보를 얻습니다.
def belt_score(elems):
    b_num = elems[1] - 1

    a = head[b_num] if head[b_num] != 0 else -1
    b = tail[b_num] if tail[b_num] != 0 else -1
    c = num_gift[b_num]

    print(a + 2 * b + 3 * c)


# 입력:
q = int(input())
for _ in range(q):
    elems = list(map(int, input().split()))
    q_type = elems[0]

    if q_type == 100:
        build_factory(elems)
    elif q_type == 200:
        move(elems)
    elif q_type == 300:
        change(elems)
    elif q_type == 400:
        divide(elems)
    elif q_type == 500:
        gift_score(elems)
    else:
        belt_score(elems)
