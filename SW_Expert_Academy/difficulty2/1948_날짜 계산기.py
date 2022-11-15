import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    month1,day1,month2,day2 = map(int,input().split())
    calendar ={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if month1 == month2:
        print(day2-day1+1)
        continue
    else:
        sum = 0
        for mon in range(month1+1,month2):
            sum += calendar[mon]
        sum += calendar[month1] - day1 + 1
        sum += day2
        print(sum)