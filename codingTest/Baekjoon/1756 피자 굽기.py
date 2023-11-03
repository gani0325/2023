"""
[1756] 피자 굽기

💛 문제
월드피자 원주 지점에서 N개의 피자 반죽을 오븐에 넣고 구우려고 한다. 
그런데, 월드피자에서 만드는 피자 반죽은 지름이 제각각이다. 그런가하면, 월드피자에서 사용하는 오븐의 모양도 몹시 오묘하다. 
이 오븐은 깊은 관처럼 생겼는데, 관의 지름이 깊이에 따라 들쭉날쭉하게 변한다. 아래는 오븐의 단면 예시이다.

피자 반죽은 완성되는 순서대로 오븐에 들어간다. 
이렇게 N개의 피자가 오븐에 모두 들어가고 나면, 맨 위의 피자가 얼마나 깊이 들어가 있는지가 궁금하다. 
이를 알아내는 프로그램을 작성하시오.

💚 입력
첫째 줄에 오븐의 깊이 D와 피자 반죽의 개수 N이 공백을 사이에 두고 주어진다. (1 ≤ D, N ≤ 300,000) 
둘째 줄에는 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름이 차례대로 주어진다. 
셋째 줄에는 피자 반죽이 완성되는 순서대로, 그 각각의 지름이 주어진다. 
오븐의 지름이나 피자 반죽의 지름은 10억 이하의 자연수이다.

💙 출력
첫째 줄에, 마지막 피자 반죽의 위치를 출력한다. 
오븐의 최상단이 1이고, 최하단 가장 깊은 곳이 D이 된다. 만약 피자가 모두 오븐에 들어가지 않는다면, 0을 출력한다.
"""

# 오븐의 깊이 D와 피자 반죽의 개수 N
d, n = map(int, input().split())

# 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름
oven = list(map(int, input().split()))

# 피자 반죽이 완성되는 순서대로, 그 각각의 지름
pizza = list(map(int, input().split()))

result = [0] * d

end = d
for i in range(n) :
    for j in range(0, end) :
        
        if oven[j] >= pizza[i] :
            if j == end - 1 :
                result[j - 1] = 1
                end = j
            continue
        else :
            result[j - 1] = 1
            end = j
            break

if sum(result) != n :
    print(-1)
else :
    for i in range(d) :
        if result[i] == 1 :
            print(i+1)
            break