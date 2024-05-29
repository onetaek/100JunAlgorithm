import sys

sys.stdin = open('input.txt','r')

t = int(sys.stdin.readline())

for _ in range(t):
  n_list = list(map(int,sys.stdin.readline().split()))
  n_list.sort(reverse=True)
  print(n_list[2])