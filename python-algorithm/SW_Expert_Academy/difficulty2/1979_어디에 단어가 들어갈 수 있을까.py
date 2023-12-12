import sys
sys.stdin = open("input.txt","r")
N = int(input())

def is_insert(puzzle_list,word_size,puzzle_size):
    len = 0
    max = 0
    cnt = 0
    is_first = True
    for i,puzzle in enumerate(puzzle_list):
        if puzzle == 1:
            if is_first == True:
                len = 1
                is_first = False
            else:#is_first == False
                len += 1
            if len >= max:
                max = len
            if i == puzzle_size -1 and max == word_size:
                cnt += 1
        else:#0일떄
            if max == word_size:
                cnt += 1
            len = 0
            max = 0
            is_first = True
    return cnt

for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    sum_cnt = 0
    puzzle_size,word_size = map(int,input().split())
    puzzle_board = []
    puzzle_board_reverse = []
    #퍼즐보드에 넣을 받을 받기
    for _ in range(puzzle_size):
        puzzle_board.append(list(map(int,input().split())))
    #뒤집어진 보드를 만들기위해 0으로 채워진 보드를 만듬
    for i in range(puzzle_size):
        temp_list = []
        for j in range(puzzle_size):
            temp_list.append(0)
        puzzle_board_reverse.append(temp_list)
    #0으로 채워진 보드에 i,j의 위치를 바꿔줘서 값을 넣어줌
    for i in range(puzzle_size):
        for j in range(puzzle_size):
            puzzle_board_reverse[j][i] = puzzle_board[i][j]
    #is_insert함수를 이용해서 각 puzzle_list들이 삽입이 되는지 확인한다.
    for puzzle_list in puzzle_board:
        cnt = is_insert(puzzle_list,word_size,puzzle_size)
        sum_cnt += cnt
    #뒤집어진 보드도 확인한다.
    for puzzle_list in puzzle_board_reverse:
        cnt = is_insert(puzzle_list,word_size,puzzle_size)
        sum_cnt += cnt
    print(sum_cnt)
        