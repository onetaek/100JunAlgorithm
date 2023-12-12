#리스트에서 값을 처음부터 temp에 넣는다.
#하나 넣을때마다 temp의 값들과 비교하면서 대소비교를한다.
#클경우에는 현재값 - temp값을 해준것을 모두더한다.
#그리고 temp를 비운다.
#계속 반복한다.
import sys
sys.stdin = open('input.txt','r')
N = int(input())

for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    case = int(input())
    num_list = list(map(int,input().split()))
    temp_list = []
    money = 0
    for num in num_list:
        temp_list.append(num)
    print(temp_list)
    

    print(money)

