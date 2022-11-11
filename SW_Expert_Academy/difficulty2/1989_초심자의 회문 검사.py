import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case}",end=" ")
    text = input()
    if text == text[::-1]:
        print(1)
    else:
        print(0)