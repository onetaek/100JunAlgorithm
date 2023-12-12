N,M = map(int,input().split())
num_list = list(map(int,input().split()))

sum_list = []
result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = num_list[i]+num_list[j]+num_list[k]
            if sum > M:
                continue
            else:
                result = max(result,sum)
print(result)