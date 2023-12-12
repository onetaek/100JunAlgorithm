n = int(input())

for i in range(n):

    sum = 0
    con = 1

    quiz = input()
    for j in quiz :
        if j =="O":
            sum += con
            con += 1
        elif j == "X":
            con = 1
    print(sum) 
