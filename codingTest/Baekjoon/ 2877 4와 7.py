"""
[2877] 4와 7

💛 문제
창영이는 4와 7로 이루어진 수를 좋아한다. 
창영이가 좋아하는 수 중에 K번째 작은 수를 구해 출력하는 프로그램을 작성하시오.

💚 입력
첫째 줄에 K(1 ≤ K ≤ 10^9)가 주어진다.

💙 출력
첫째 줄에 창영이가 좋아하는 숫자 중 K번째 작은 수를 출력한다.
"""

# K번째 작은 수
k = int(input())

num = 0
cnt = 0


while(1) :
    num += 1
    temp = []

    for j in str(num):
        temp.append(int(j))

    if 1 in temp :
        continue
    
    elif 2 in temp :
        continue
    
    elif 3 in temp :
        continue
    
    elif 5 in temp :
        continue

    elif 6 in temp :
        continue
    
    elif 8 in temp :
        continue
    
    elif 9 in temp :
        continue
    
    elif 0 in temp :
        continue

    else :
        cnt += 1

    if cnt == k :
        print(num)
        break