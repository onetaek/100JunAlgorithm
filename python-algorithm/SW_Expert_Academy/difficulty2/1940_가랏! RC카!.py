import sys
sys.stdin = open("input.txt","r")
T = int(input())
for test_case in range(1,T+1):
    print(f"#{test_case}",end=" ")
    N = int(input())
    V = 0
    sum_V = 0
    for _ in range(N):
        # 1이면 이전의 속도에서 +받은값
        # 0이면 이전의값 유지
        # 2이면 이전의 속도에서 -받은값
        data_list = list(map(int,input().split()))
        
        if data_list[0] == 0:
            pass
        elif data_list[0] == 1:
            V += data_list[1]
        elif data_list[0] == 2:
            if V - data_list[1] < 0:
                V = 0
            else :
                V -= data_list[1]
        sum_V += V
    print(sum_V)
