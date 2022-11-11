import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    P,Q,R,S,W = map(int,input().split())
    A_sa = W * P
    if W > R:
        B_sa = Q + (W-R) * S
    else:
        B_sa = Q
    if A_sa > B_sa:
        print(B_sa)
    else:
        print(A_sa)
