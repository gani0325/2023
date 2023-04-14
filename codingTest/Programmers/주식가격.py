# 주식가격
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수

def solution(prices):
    answer = []
    for i in range(len(prices) - 1) :
        temp = len(prices) - i - 1
        for j in range(1+i, len(prices)) :
            if prices[i] > prices[j] :
                temp = j - i
                break
        answer.append(temp)
    answer.append(0)
    return answer