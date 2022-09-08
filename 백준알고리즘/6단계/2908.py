A,B = input().split()
A,B = A[::-1],B[::-1]
if int(A) > int(B):
    print(A)
elif int(B) > int(A):
    print(B)