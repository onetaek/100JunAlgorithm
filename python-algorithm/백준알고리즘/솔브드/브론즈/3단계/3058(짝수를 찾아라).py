import sys

# sys.stdin = open('input.txt','r')

t = int(sys.stdin.readline())

for _ in range(t):
  number_list = list(map(int,sys.stdin.readline().split()))

  sum_of_even = 0
  min_even = -1

  for number in number_list:
    if number % 2 == 0:
      sum_of_even += number

      if min_even == -1 or number < min_even:
        min_even = number

  print(f'{sum_of_even} {min_even}')