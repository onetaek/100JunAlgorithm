import math

def solution(a):
    prime_sum = 0
    
    for num in range(2, a + 1):
        is_prime = True
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_sum += num
    
    return prime_sum

# 테스트
print(solution(5))  # 출력: 10
print(solution(10))  # 출력: 17
print(solution(30))  # 출력: 129