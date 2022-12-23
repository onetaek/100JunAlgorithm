import sys
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(num_list)/N))

#중앙값
num_list.sort()
mid_idx = N//2
print(int(num_list[mid_idx]))

#최빈값
count_list = [0]*8001
for num in num_list:
    count_list[num] += 1
max_list = []
for i,count in enumerate(count_list):
    if count == max(count_list):
        max_list.append(i)
for i in range(len(max_list)):
    if max_list[i] > 4000:
        max_list[i] -= 8001
max_list.sort()
if len(max_list) < 2:
    print(max_list[0])
else:
    print(max_list[1])

#범위
print(max(num_list)-min(num_list))




