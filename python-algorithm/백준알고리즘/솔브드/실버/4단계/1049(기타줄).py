import sys

# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n, m = map(int, input().split(' '))

price_per_6 = 1001 
price_per_1 = 1001
for i in range(m):
  p, s = map(int, input().split(' '))
  price_per_6 = min(price_per_6, p)
  price_per_1 = min(price_per_1, s)

result = 0


if price_per_6 > price_per_1*6:
  result += n * price_per_1
else:
  result += (n//6) * price_per_6

  if (n%6)*price_per_1 > price_per_6:
    result += price_per_6
  else:
    result+= (n%6)*price_per_1

print(result)