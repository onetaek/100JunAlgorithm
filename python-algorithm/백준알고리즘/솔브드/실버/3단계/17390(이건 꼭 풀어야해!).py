# https://www.acmicpc.net/problem/17390

import sys

# sys.stdin = open("input.txt", "r")
N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

for i in range(1, len(A)):
  A[i] = A[i] + A[i-1]


for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    if L == 1:
       print(A[R - 1])
    else:
       print(A[R - 1] - A[L - 2])    