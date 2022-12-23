T = int(input())

def next_k(num_list):
    temp_list = []

    for i in range(len(num_list)):
        temp_list.append(0)

    for i in range(0,len(num_list)):
        for j in range(i+1):
            temp_list[i] += num_list[j]    
    
    for i in range(len(num_list)):
        num_list[i] = temp_list[i]


for _ in range(T):
    k = int(input())
    n = int(input())
    num_list = []
    for i in range(1,n+1):
        num_list.append(i)
    
    for _ in range(k):
        next_k(num_list)
    
    print(num_list[n-1])
    
    
    
