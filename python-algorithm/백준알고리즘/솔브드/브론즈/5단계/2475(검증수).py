import sys

# sys.stdin = open('input.txt','r')

number_list = list(map(int,sys.stdin.readline().split()))

sum = 0
for number in number_list:
  sum += number * number

print(sum%10)