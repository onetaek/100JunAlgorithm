import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    num_list = list(map(int,input().split()))
    sum = 0
    cnt = len(num_list)
    print(f"#{test_case}",end=" ")
    for num in num_list:
        sum += num
    print(round(sum/cnt))