import sys

def gcd(a,b):
  while(b != 0):
    a, b = b, a % b
  return a

# sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
ring_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(ring_list)):
  gcd_number = gcd(ring_list[0], ring_list[i])
  print(f"{ring_list[0]//gcd_number}/{ring_list[i]//gcd_number}")