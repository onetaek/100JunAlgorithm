n = int(input())
for _ in range(n):
    num, str = input().split()
    for i in str:
        print(i*int(num), end="")
    print()
    