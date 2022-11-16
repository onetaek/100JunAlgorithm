import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case}",end=" ")
    M,N = map(int,input().split())
    M_list = list(map(int,input().split()))
    N_list = list(map(int,input().split()))
    long_len = 0
    short_len = 0
    long_list = []
    short_list = []
    if M > N:
        long_list = M_list
        short_list = N_list
        long_len = M
        short_len = N
    else:
        long_list = N_list
        short_list = M_list
        long_len = N
        short_len = M
    
    sum_list = []
    
    for i in range(long_len - short_len+1):
        sum = 0
        for j in range(short_len):
            sum += long_list[j] * short_list[j]
        sum_list.append(sum)
        long_list.pop(0)
    print(max(sum_list))
    
        
