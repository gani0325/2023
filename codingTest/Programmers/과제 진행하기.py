# 과제 진행하기
# 과제를 받은 루는 다음과 같은 순서대로 과제를 하려고 계획을 세움
#   과제는 시작하기로 한 시각이 되면 시작
#   새로운 과제를 시작할 시각이 되었을 때, 
#       기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작
#   진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행
#       만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 
#       새로 시작해야 하는 과제부터 진행
#   멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작
# 과제 계획을 담은 이차원 문자열 배열 plans가 매개변수로 주어질 때, 
# 과제를 끝낸 순서대로 이름을 배열에 담아 return 하는 solution 함수

def solution(plans):
    # name : 과제의 이름, start : 과제의 시작 시각, playtime : 과제를 마치는데 걸리는 시간 (분)
    # "00:00" ~ "23:59"
    finish = []
    yet = []
    answer = []
    
    # 과제 시간 이른 순으로 정렬
    plans.sort(key = lambda x : x[1])
    for i in range(len(plans)) :
        a, b = plans[i][1].split(":")
        a = int(a)
        b = int(b)
        c = int(plans[i][2])
        next = b + c
        
        if next >= 60 :
            temp = next // 60
            a += temp
            b = next - 60 * temp
            if a >= 24 :
                a = a - 24
        else :
            b = b + c
        
        if a < 10 :
            a = str(0) + str(a)
        elif b < 10 :
            b = str(0) + str(b)

        fis = str(a) + ":" + str(b)
        finish.append(fis)

    for i in range(1, len(plans)) :        
        if plans[i][1] < finish[i-1] :           
            yet.append(plans[i-1][0])
        else :
            answer.append(plans[i-1][0])      
    answer.append(plans[-1][0])
    yet.reverse()
    
    answer.extend(yet)
    return answer