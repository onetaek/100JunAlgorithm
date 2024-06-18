import sys
sys.stdin = open('input.txt','r')

earth, sun, month = map(int, input().split()) # 15, 28, 19

year = 1

while(True):
  if ((year - earth) % 15 == 0) and  ((year - sun) % 28 == 0) and ((year - month) % 19 == 0):
    break
  year += 1

print(year)