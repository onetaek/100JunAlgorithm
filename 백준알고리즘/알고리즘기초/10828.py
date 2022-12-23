import sys
sys.stdin = open("input.txt","r")
T = int(input())
myStack = []

board = []
for _ in range(T):
    temp_list = list(input().split())
    board.append(temp_list)

for myList in board:
    if myList[0] == "push":
        myStack.append(myList[1])
    elif myList[0] == "top":
        if myStack == []:
            print("-1")
        else:
            print(myStack[len(myStack)-1])
    elif myList[0] == "pop":
        if len(myStack) == 0:
            print("-1")
        else:
            print(myStack.pop())
    elif myList[0] == "empty":
        if myStack == []:
            print("1")
        else:
            print("0")
    elif myList[0] == "size":
        print(len(myStack))
    

