# 다리를 지나는 트럭
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 함
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내기
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딤
#   다리에 완전히 오르지 않은 트럭의 무게는 무시
# 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수

def solution(bridge_length, weight, truck_weights):
    time = 0
    # # 트럭 무게
    # truck = list(truck_weights) 
    # 다리 트럭 수
    bridge = [0] * bridge_length 
    # 다리 위의 총 트럭 무게
    temp = 0
    
    while (bridge):
        time += 1
        temp -= bridge.pop(0)
        if truck_weights:
            # 트럭 무게가 다리 버티는 무게보다 작을 때 (여유)
            if ( temp + truck_weights[0] ) <= weight:
                temp += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0) # 여유 없으면 무게 0 추가

    return time