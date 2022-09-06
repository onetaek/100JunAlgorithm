def d(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return int(n) + sum

arr = []
for i in range(10000):
    if(d(i)<10000):
        arr.append(d(i))
arr = list(set(arr))

notin_arr = []
for i in range(10000):
    if i not in arr:
        notin_arr.append(i)

for i in notin_arr:
    print(i)
  