# 순열과 조합
# 순열 : 서로 다른 n개에서 r를 선택하여 일렬로 나열
# 조합 : 서로 다룬 n개에서 순서에 상관없이 서로 다른 r개를 선택

# 순열
import itertools

data = [1, 2]

for x in itertools.permutations(data, 2) :
    print(list(x))



# 조합
import itertools

data = [1, 2, 3]

for x in itertools.combinations(data, 2) :
    print(list(x), end = "")