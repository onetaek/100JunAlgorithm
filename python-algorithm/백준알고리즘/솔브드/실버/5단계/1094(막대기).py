X = int(input())
count = 0

while X > 0:
    remainder = X % 2
    if remainder == 1:
        count += 1
    X //= 2

print(count)