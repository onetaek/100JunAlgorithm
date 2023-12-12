import sys
sys.stdin = open("input.txt","r")

password, num = map(int,input().split())
cnt = 1
while password != num:
    cnt += 1
    num += 1
print(cnt)