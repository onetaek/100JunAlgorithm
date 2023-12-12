import sys
sys.stdin = open("input.txt","r")
T = int(input())
for test_case in range(1,T+1):
    print(f"#{test_case}",end=" ")
    A,B = map(int,input().split())
    print(A//B,A%B)