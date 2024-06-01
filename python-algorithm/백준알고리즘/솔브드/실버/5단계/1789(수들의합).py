s = int(input())

result = 0
count = 0

while True:
    count += 1
    result += count
    
    if result > s:
        break

print(count-1)