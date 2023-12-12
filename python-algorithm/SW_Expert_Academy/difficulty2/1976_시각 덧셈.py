import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    time_list = list(map(int,input().split()))
    hour = time_list[0] + time_list[2]
    minute = time_list[1] + time_list[3]
    if minute >= 60:
        hour += 1
        minute -= 60
    if hour > 12:
        hour -= 12
    print(hour, minute)

