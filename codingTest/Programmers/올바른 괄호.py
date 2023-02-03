# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 
# 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수


def solution(s) :
    stack = []
    
    for i in s :
        if i == "(" :
            stack.append(i)
        else :
            if stack :          # 양수일 경우
                stack.pop()     # 뒤에꺼 뺌
            else :              # 비어있다면
                return False
    if stack :      # 양수일 경우
        return False
    return True