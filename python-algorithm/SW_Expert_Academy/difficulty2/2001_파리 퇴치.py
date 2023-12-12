import sys
sys.stdin = open("input.txt","r")
N = int(input())
def fly_sum(fly_list,start_i,start_j,stick):
    sum = 0
    for i in range(start_i,start_i+stick):
        for j in range(start_j,start_j+stick):
            sum += fly_list[i][j]
    return sum
for test_case in range(1,N+1):
    print(f"#{test_case}",end=" ")
    max = 0
    space, stick = map(int,input().split())
    fly_list = []
    for _ in range(space):
        temp_list = list(map(int,input().split()))
        fly_list.append(temp_list)
    for i in range(space-stick+1):
        for j in range(space-stick+1):
            flies = fly_sum(fly_list,i,j,stick)
            if flies > max :
                max = flies
    print(max)
            