def solution(N,K):
    
    num_list = []
    for i in range(1,N+1):
        num_list.append(i)
    num_list = num_list * N
    count = 0
    while True :
        #----제거하다보면 18번째 줄에 num_list[K-1]에 리스트의 길이가 짧아져서 여기서 오류가 떠서 조건을 추가해줬어
        if len(num_list) < K:
            print('if문')
            print('if문의 num_list',num_list)
            cnt = 1
            while len(num_list) < K:
               num_list *= cnt
               cnt += 1  
        #--------------------------------------------------------------------------------------------------
        if num_list[0] == num_list[1]:
            return num_list[0]
        print('num_list',num_list)
        temp = num_list[K-1]
        num_list = num_list[K-1:]
        while temp in num_list:
            num_list.remove(temp)
print(solution(50,7))