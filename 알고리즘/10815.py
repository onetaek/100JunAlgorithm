N = int(input())
my_list = list(map(int,input().split()))
M = int(input())
num_list = list(map(int,input().split()))

set_my_list = set(my_list)

for num in num_list:
    if num in set_my_list:
        print(1,end=' ')
    else:
        print(0,end=' ')
