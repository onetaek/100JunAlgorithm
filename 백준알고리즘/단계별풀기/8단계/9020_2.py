# 골드바흐의 추측
# 뭔가...골드바흐의 추측의 원리를 알아야 풀 수 있는 느낌?
def isSoSu(n):
    if n==1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())

    A, B = n//2,n//2
    while(A>0):
        if isSoSu(A) and isSoSu(B):
            print(A,B)
            break
        else:
            A -=1
            B +=1