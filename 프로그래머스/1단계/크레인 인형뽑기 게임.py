def solution(board, moves):
    answer = 0
    my_board = [[] for i in range(len(board))]
    for i in range(len(board)-1,-1,-1):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                my_board[j].append(board[i][j])

    print(my_board)

    my_stack = []

    for num in moves:
        if len(my_board[num-1]) != 0:
            temp = my_board[num-1][len(my_board[num-1])-1]
            my_stack.append(temp)
            
            my_board[num-1].remove(my_board[num-1][len(my_board[num-1])-1]) 
    
    print(my_board)
    print(my_stack)

    while True:
        isAnswer = True
        for i in range(len(my_stack)-1):
            
            if my_stack[i] == my_stack[i+1]:
                isAnswer = False
                del my_stack[i+1]
                del my_stack[i]
                answer += 2
                break 
        if isAnswer == True:
            break
    
    print(my_stack)
    print(answer)

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))