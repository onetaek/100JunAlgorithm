import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case}",end=" ")
    student_cnt, K = map(int,input().split())
    student_list = []
    for _ in range(student_cnt):
        student_list.append(list(map(int,input().split())))
    student_score_list = []
    for i,student in enumerate(student_list):
        sum = student[0] * 35 + student[1] * 45 + student[2] * 20
        student_score_list.append([sum,i])
    student_score_list.sort(reverse=True)
    
    rank = 0
    for i,student_score in enumerate(student_score_list):
        if student_score[1]+1 == K:
            rank = i+1
    
    if rank >=1 and rank <= student_cnt/10 * 1:
        print("A+")
    elif rank <= student_cnt/10 * 2:
        print("A0")
    elif rank <= student_cnt/10 * 3:
        print("A-")
    elif rank <= student_cnt/10 * 4:
        print("B+")
    elif rank <= student_cnt/10 * 5:
        print("B0")
    elif rank <= student_cnt/10 * 6:
        print("B-")
    elif rank <= student_cnt/10 * 7:
        print("C+")
    elif rank <= student_cnt/10 * 8:
        print("C0")
    elif rank <= student_cnt/10 * 9:
        print("C-")
    elif rank <= student_cnt/10 * 10:
        print("D0")
    