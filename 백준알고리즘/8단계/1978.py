N = int(input())
num_list = list(map(int,input().split()))
sosoo_list = []

for i in range(1,1001):
    sosoo = []
    for j in range(1,i+1):
        if i % j == 0:
            sosoo.append(j)
    if len(sosoo) == 2:
        sosoo_list.append(i)

count = 0

for i in sosoo_list:
    for j in num_list:
        if i == j:
            count += 1
    
print(count)