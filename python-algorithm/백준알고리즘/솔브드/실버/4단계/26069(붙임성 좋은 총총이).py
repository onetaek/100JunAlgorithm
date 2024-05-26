import sys

sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())

dancing_people = {'ChongChong'}

for _ in range(n):
  a, b = map(str, sys.stdin.readline().split())
  if a in dancing_people:
        dancing_people.add(b)
  if b in dancing_people:
      dancing_people.add(a)

print(len(dancing_people))