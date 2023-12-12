A,B = map(int,input().split())

# 가위는 1, 바위는 2, 보는 3

if (A == 1 and B == 3) or (A == 2 and B == 1) or (A ==3 and B ==2)  :
    print("A")
elif (A == 1 and B == 2) or (A == 2 and B == 3) or (A == 3 and B == 1) :
    print("B")

