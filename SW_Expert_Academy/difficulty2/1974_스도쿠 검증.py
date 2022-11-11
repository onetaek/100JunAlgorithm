import sys
sys.stdin = open("input.txt","r")
N = int(input())

def board3x3_to_list(start_i,start_j,board):
    list= [0] * 9
    idx = 0
    for i in range(start_i,start_i+3):
        for j in range(start_j,start_j+3):
            list[idx] = board[i][j]
            idx += 1
    return list

def is_pass(board):
    is_right = True
    for list in board:
        check_list= [1,2,3,4,5,6,7,8,9]
        list.sort()
        for i in range(9):
            if check_list[i] != list[i]:
                is_right = False
                break
    return is_right


for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    #스도쿠검증결과
    is_right = True
    #평범한 스도쿠보드
    sdoq_board = []
    for _ in range(9):
        temp_list = list(map(int,input().split()))
        sdoq_board.append(temp_list)
    #뒤집은 스도쿠보드
    reverse_sdoq_board = []
    for _ in range(9):
        reverse_sdoq_board.append([0]*9)
    for i in range(9):
        for j in range(9):
            reverse_sdoq_board[i][j] = sdoq_board[j][i]
    #3x3크기별로 리스트로 만들어서 만든 보드
    sdoq_board_3x3 = []
    for i in range(0,9,3):
        temp_list = []
        for j in range(0,9,3):
            temp_list = board3x3_to_list(i,j,sdoq_board)
            sdoq_board_3x3.append(temp_list)
    
    if is_pass(sdoq_board) == False:
        is_right = False
        print(0)
        continue
    
    if is_pass(reverse_sdoq_board) == False:
        is_right = False
        print(0)
        continue
    
    if is_pass(sdoq_board_3x3) == False:
        is_right = False
        print(0)
        continue
        
    print(1)