# 숫자 N은 아래와 같다.
# N=2a x 3b x 5c x 7d x 11e
# N이 주어질 때 a, b, c, d, e 를 출력하라.
import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case}",end=" ")
    num = int(input())
    sosu_list = [2,3,5,7,11]
    sosu_cnt_list = [0,0,0,0,0]
    for i,sosu in enumerate(sosu_list):
        while True :
            if num % sosu == 0:      
                num //= sosu
                sosu_cnt_list[i]+=1
            else:
                break
    for sosu_cnt in sosu_cnt_list:
        print(sosu_cnt,end=" ")
    print()        
    
    

