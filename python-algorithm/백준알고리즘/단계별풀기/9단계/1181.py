import sys
N = int(sys.stdin.readline())
word_list = []
for _ in range(N):
    temp = sys.stdin.readline().strip()
    if temp not in word_list:
        word_list.append(temp)

word_list.sort()
word_list.sort(key= len)

for i in word_list:
    print(i)
