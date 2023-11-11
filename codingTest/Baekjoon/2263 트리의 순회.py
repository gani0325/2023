"""
[2263] 트리의 순회

💛 문제
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 
이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

💚 입력
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 
다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 
그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

💙 출력
첫째 줄에 프리오더를 출력한다.
"""

# 1) 후위순회에서 마지막에 오는 값은 트리의 루트
# 2) 중위순회에서 루트를 기준으로 왼쪽 서브 트리와 오른쪽 서브 트리
# 3) 후위순회를 중위순회와 같이 나눈 후 각 서브 트리에서 마지막에 오는 값은 서브 트리의 루트

# 파이썬의 재귀 최대 깊이의 기본 설정이 1,000회 이기 때문에 런타임 에러가 발생
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# inorder의 값 index 리스트
inorder_pos = [0] * (n+1)

def preorder(inorder_s, inorder_e, postorder_s, postorder_e):
    # 재귀함수 종료 조건
    if (inorder_s > inorder_e) or (postorder_s > postorder_e):
        return
    
    # 후위 순회의 마지막 노드 출력
    p = postorder[postorder_e]
    print(p, end =' ')
    
    # 왼쪽 서브트리 노드의 개수
    left = inorder_pos[p] - inorder_s

    # 오른쪽 서브트리 노드의 개수
    right = inorder_e - inorder_pos[p]
    
    # 왼쪽 서브 트리
    preorder(inorder_s, inorder_s+left-1, postorder_s, postorder_s+left-1)
    # 오른쪽 서브 트리
    preorder(inorder_e - right + 1, inorder_e, postorder_e - right, postorder_e - 1)


# 후위순회의 마지막값이 중위순회 몇번째에 존재하는지 알기 위해
for i in range(n):
    inorder_pos[inorder[i]] = i
    
preorder(0, n-1, 0, n-1)