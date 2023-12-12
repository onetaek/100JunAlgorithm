n = int(input())

print("#첫번째 버전")
for num in range(1, n + 1):
  print("*" * num)

print("#두번째 버전")
for i in range(n):
  for j in range(i+1):
    print("*",end="")
  print()


