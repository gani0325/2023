# 변속기가 1단에서 8단으로 연속적으로 변속을 한다면 ascending
# 8단에서 1단으로 연속적으로 변속한다면 descending
# 둘다 아니라면 mixed

# 변속한 순서가 주어졌을 때 이것이 ascending인지, descending인지, 아니면 mixed인지 출력

import sys

result = list(map(int, input().split()))
descending = sorted(result, reverse=True)
ascending = sorted(result)
# print(result)
# print(descending)
# print(ascending)
if result == descending:
    print("descending")
elif result == ascending:
    print("ascending")
else:
    print("mixed")
