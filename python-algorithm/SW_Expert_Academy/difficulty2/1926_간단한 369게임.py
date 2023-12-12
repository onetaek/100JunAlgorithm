import sys
sys.stdin = open("input.txt","r")

N = int(input())
for num in range(1,N+1):
    cnt = 0
    for num_str in str(num):
        if int(num_str)%3 == 0 and int(num_str) != 0:
            cnt += 1
    if cnt == 0:
        print(num,end=" ")
    else:
        print("-"*cnt,end=" ")
