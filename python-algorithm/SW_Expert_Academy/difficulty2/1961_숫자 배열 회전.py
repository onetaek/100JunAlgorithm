import sys
sys.stdin = open("input.txt","r")
N = int(input())

def rotate90(board,empty_board):
    i_idx = 0
    j_idx = 0
    for j in range(len(board)):
        for i in range(len(board)-1,-1,-1):
            empty_board[i_idx][j_idx] = board[i][j]
            j_idx += 1
        i_idx += 1
        j_idx = 0
    return empty_board

def clear_list(list):
    for i in range(len(list)):
        for j in range(len(list)):
            list[i][j] = 0
    return list

def insert_val(new_list,prev_list):
    n = len(new_list)
    for i in range(n):
        for j in range(n):
            new_list[i][j] = prev_list[i][j]
    return new_list

for test_case in range(1,N+1):
    print(f"#{test_case}")
    num = int(input())
    board_first = []
    degree90 = []
    degree180 = []
    degree270 = []
    empty_board = []
    
    for _ in range(num):
        temp_list = list(map(int,input().split()))
        board_first.append(temp_list)

    for _ in range(num):
        empty_board.append([0]*num)
    for _ in range(num):
        degree90.append([0]*num)
    for _ in range(num):
        degree180.append([0]*num)
    for _ in range(num):
        degree270.append([0]*num)
    
    temp_list = rotate90(board_first,empty_board)
    insert_val(degree90,temp_list)
    clear_list(temp_list)

    temp_list = rotate90(degree90,empty_board)
    insert_val(degree180,temp_list)
    clear_list(temp_list)


    temp_list = rotate90(degree180,empty_board)
    insert_val(degree270,temp_list)
    clear_list(temp_list)


    for i in range(num):
        for j in range(num):
            print(degree90[i][j],end="")
        print("",end=" ")
        for j in range(num):
            print(degree180[i][j],end="")
        print("",end=" ")
        for j in range(num):
            print(degree270[i][j],end="")
        print()

    
