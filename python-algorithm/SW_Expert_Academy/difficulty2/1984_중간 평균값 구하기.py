import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    num_list = list(map(int,input().split()))
    num_list.sort()
    num_list = num_list[1:len(num_list)-1]
    sum = 0
    for num in num_list:
        sum += num
    print(round(sum/len(num_list)))
