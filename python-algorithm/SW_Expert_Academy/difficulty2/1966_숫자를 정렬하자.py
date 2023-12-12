import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    num_len = int(input())
    num_list = list(map(int,input().split()))
    num_list.sort()
    for num in num_list:
        print(num,end=" ")
    print()