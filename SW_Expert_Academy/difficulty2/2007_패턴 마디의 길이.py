import sys
sys.stdin = open("input.txt","r")

N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    str = input()
    start = str[0]
    cnt = 0
    for s in str:
        if s == start:
            cnt +=1
    print(cnt)