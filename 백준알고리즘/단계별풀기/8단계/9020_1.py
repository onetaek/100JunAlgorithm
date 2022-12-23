def isSoSu(n):
    if n==1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

soSu_list = []

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n):
        if isSoSu(i):
            soSu_list.append(i)

    partition_list = []

    for i in soSu_list:
        for j in soSu_list:
            if i + j == n:
                
                partition_list.append([i,j])
    
    distance_list = []

    for partition in partition_list:
        distance_list.append(abs(partition[0]-partition[1]))

    for i, distance in enumerate(distance_list):
        if distance == min(distance_list):
            print(partition_list[i][0],partition_list[i][1])
            break
    

