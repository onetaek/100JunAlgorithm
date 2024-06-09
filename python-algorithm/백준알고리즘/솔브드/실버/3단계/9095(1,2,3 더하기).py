import sys

#sys.stdin = open('input.txt','r')

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  dp_list = [0] * (n + 1)
  
  for i in range(1, n  + 1):
    if i == 1:
      dp_list[i] = 1
    elif i == 2:
      dp_list[i] = 2
    elif i == 3:
      dp_list[i] = 4
    else:
      dp_list[i] = dp_list[i - 1] + dp_list[i - 2] + dp_list[i - 3]
  print(dp_list[n])