import sys

#sys.stdin = open('input.txt','r')

n = str(sys.stdin.readline())

last_index = len(n) - 1

sum = 0

for i in range(last_index):
    sum += 9 * (10 ** i) * (i + 1)
    i += 1
sum += ((int(n) - (10 ** last_index)) + 1) * (last_index + 1)

print(sum)