num_list = []
N = int(input())
for _ in range(N):
    num_list.append(int(input()))

for i in range(len(num_list)):
    for j in range(i,len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i],num_list[j] = num_list[j],num_list[i]

for i in num_list:
    print(i)