
# 입력 받기
n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열

n = len(arr)    
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) 