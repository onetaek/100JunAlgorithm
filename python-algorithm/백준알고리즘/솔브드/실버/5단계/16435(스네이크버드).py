import sys

#sys.stdin = open("input.txt","r")

n, l = map(int, sys.stdin.readline().split())
fruit_list = list(map(int, sys.stdin.readline().split()))
fruit_list.sort()

for fruit in fruit_list:
  if fruit <= l:
    l += 1
  else:
    break

print(l)