import sys
sys.stdin = open("input.txt","r")
T = int(input())
for test_case in range(1,T+1):
    print(f"#{test_case}",end=" ")
    N = int(input())
    for _ in range(N):
        # 1이면 이전의 속도에서 +받은값
        # 0이면 이전의값 유지
        # 2이면 이전의 속도에서 -받은값
        V = 0
        
        data_list = list(map(int,input().split))
        
        if data_list[0] == 0:
            pass
        elif data_list[0] == 1:
            V += data_list[1]
        elif data_list[0] == 2:
            V -= data_list[1]
