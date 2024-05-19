def changesum(arr):
    ans = 0
    for i in range(len(arr)):
        ans += int(arr[i])
    return ans

numbers = []
for j in range(1, 10001):
    jun = list(str(j))
    num = j + changesum(jun)
    numbers.append(num)
for k in range(1, 10001):
    if k not in numbers:
        print(k)