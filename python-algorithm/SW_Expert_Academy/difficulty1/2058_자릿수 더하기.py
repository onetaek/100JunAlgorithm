import sys
sys.stdin = open("input.txt", "r")

num = int(input())
num = str(num)
sum = 0
for n in num:
    sum += int(n)

print(sum)