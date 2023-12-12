def fact(N):
    if N < 2:
        return 1
    else:
        return fact(N-1)*N
N = int(input())
print(fact(N))