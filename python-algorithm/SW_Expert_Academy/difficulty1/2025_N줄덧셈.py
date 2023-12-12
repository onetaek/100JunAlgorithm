N = int(input())
def fact(N):
    if N == 1:
        return N
    return N + fact(N-1)
print(fact(N))
