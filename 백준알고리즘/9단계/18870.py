import sys
N = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
num_list_sorted = sorted(list(set(num_list)))


num_dict = {}
for i,num in enumerate(num_list_sorted):
    num_dict[num] = i

for num in num_list:
    print(num_dict[num],end=' ')