# 소수의 판별
# : 2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수


def is_prime_number(x) :
    # 2부터 (x-1) 까지의 모든 수
    for i in range(2, x) :
        if x % i == 0:
            return False
    return True