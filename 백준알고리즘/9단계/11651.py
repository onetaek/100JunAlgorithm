import sys
N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(list(map(int,sys.stdin.readline().split())))

def change(num_list):
    for i in range(len(num_list)):
        num_list[i][0],num_list[i][1] = num_list[i][1],num_list[i][0]
    return num_list

num_list = change(num_list)
num_list.sort()
num_list = change(num_list)

for i in range(len(num_list)):
    print(num_list[i][0],num_list[i][1])
