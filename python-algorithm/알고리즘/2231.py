def constructor(N):
    sum = 0
    for i in N:
        sum += int(i)
    return int(N) + sum

N = input()    
con_list = []

N_int = int(N)

for i in range(1,N_int+1):
    con = constructor(str(i))
    if con == N_int :
        print(i)
        break
    if i == N_int:
        print(0)
        break
        


# print(constructor(N))
