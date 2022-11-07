# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 
# 프로그램을 작성하라.
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}",end=" ")
    A,B = map(int,input().split())
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")
