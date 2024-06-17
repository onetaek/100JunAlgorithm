import sys

# sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for num in arr:
  print(1) if num in a else print(0)