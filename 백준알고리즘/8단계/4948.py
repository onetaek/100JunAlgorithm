def isSoSu(n):
    if n == 1:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

soSu_list = []
for i in range(2,246912):
    if isSoSu(i):
        soSu_list.append(i)

n = int(input())
while n > 0 :
    count = 0
    for i in soSu_list:
        if i > n and i <= 2*n:
            count += 1
    print(count)
    n = int(input())