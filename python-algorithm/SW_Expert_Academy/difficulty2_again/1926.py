import sys
sys.stdin = open("input.txt","r")

N = int(input())

for number in range(1, N+1):
    num = str(number)
    cnt = 0
    for n in num:
        if int(n)%3==0 and int(n) != 0:
            cnt += 1
    if cnt == 0 :
        print(num,end=" ")
    else :
        print(cnt*"-", end=" ")
    