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
        if myList == []:
            print("null")
        else:
            print(myStack[len(myStack)-1])
    elif myList[0] == "pop":
        if myList is None:
            print("null")
        else:
            print(myStack)
            print("!!!!!!",len(myStack))
            print(myStack[len(myStack)-1])
            myStack.remove(myStack[len(myStack)-1])
    elif myList[0] == "empty":
        if myList == []:
            print("1")
        else:
            print("0")
    elif myList[0] == "size":
        print(len(myStack))
    

