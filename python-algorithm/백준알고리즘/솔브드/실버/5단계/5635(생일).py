import sys
#sys.stdin = open('input.txt','r')

p_list = []

for _ in range(int(sys.stdin.readline())):
  name, day, month, year = sys.stdin.readline().split()
  day, month, year = map(int, (day, month, year))
  p_list.append((year, month, day, name))

p_list.sort()

print(p_list[-1][3])
print(p_list[0][3])