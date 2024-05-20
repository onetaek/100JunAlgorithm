import sys

# sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split()) 

account_dict = {}

for _ in range(n):
  site, password = sys.stdin.readline().split()
  account_dict[site] = password

for _ in range(m):
  site = sys.stdin.readline().strip()
  password = account_dict[site]
  print(password)