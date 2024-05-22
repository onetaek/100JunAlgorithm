import sys

# sys.stdin = open('input.txt','r')
a, b = sys.stdin.readline().split()

start_index = 0

min_diff_count = 99
while((start_index + len(a)) <= len(b)):
  j = 0
  diff_count = 0

  for i in range(start_index, start_index + len(a)):
    if a[j] != b[i]:
      diff_count += 1
    j += 1
  
  if diff_count < min_diff_count:
    min_diff_count = diff_count
  start_index += 1

print(min_diff_count)