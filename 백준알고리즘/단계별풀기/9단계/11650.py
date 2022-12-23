import sys
N = int(sys.stdin.readline())
num_list = []
for i in range(N):
    num_list.append(list(map(int,sys.stdin.readline().split())))

num_list.sort()
for i in range(len(num_list)):
    print(num_list[i][0],num_list[i][1])
    