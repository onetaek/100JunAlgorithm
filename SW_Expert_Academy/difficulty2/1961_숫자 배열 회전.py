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

for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
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
    
    degree90 = rotate90(board_first,empty_board)
    degree180 = rotate90(degree90,empty_board)
    degree270 = rotate90(degree180,empty_board)
    
    print(degree90)
    print(degree180)
    print(degree270)

    for J in range(len(degree90)):
        for i in range(len(degree90)):
          pass 
