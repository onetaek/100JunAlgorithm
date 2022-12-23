def han(N):
    if N<100:
        return 1
    N = str(N)
    distance = []
    for i in range(1,len(N)):
        distance.append(int(N[i])-int(N[i-1]))
    for i in range(1,len(distance)):
        if distance[0] != distance[i]:
            return 0
        else:
            return 1

N = int(input())
cnt = 0
for i in range(1,N+1):
    cnt += han(i)
print(cnt)