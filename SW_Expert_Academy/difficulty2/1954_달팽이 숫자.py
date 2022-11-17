import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    num = int(input())
    empty_list = []
    for _ in range(num):
        empty_list.append([0]*num)
    
    

    print(empty_list)