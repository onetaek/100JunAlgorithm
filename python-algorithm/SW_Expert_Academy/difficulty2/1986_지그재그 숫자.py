import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case}",end=" ")
    max_num = int(input())
    sum = 0
    is_plus = True
    for num in range(1,max_num+1):
        if is_plus:
            sum += num
            is_plus = False
        else:
            sum -= num
            is_plus = True
    print(sum)
