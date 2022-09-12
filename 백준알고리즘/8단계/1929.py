# 에라토스테네스의 체
# 1 ~ n 까지의 소수를 알아보고 싶다면 n까지의 모든 수를 다 나눠 볼 필요가 없이
# n^(1/2)이하의 수 까지만 체크해도 소수를 모두 확인할 수 있다.
M , N = map(int,input().split())
    
for num in range(M,N+1):
    if num == 1:
        continue       
    for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                break
    else:
        print(num)
    

        