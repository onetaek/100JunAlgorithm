N = int(input())

soInSu_list = []

while(N != 1):
    for i in range(2,N+1):
        if N % i == 0:
            soInSu_list.append(i)
            N = N // i
            break

for i in soInSu_list:
    print(i)