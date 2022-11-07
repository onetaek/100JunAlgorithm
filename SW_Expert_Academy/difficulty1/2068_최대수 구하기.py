import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}",end=" ")
    max = 0
    num_list = list(map(int,input().split()))
    for num in num_list:
        if num > max:
            max = num
    print(max)