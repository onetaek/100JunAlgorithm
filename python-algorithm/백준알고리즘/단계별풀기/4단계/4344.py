n = int(input())
for _ in range(n):
    sum = 0
    count = 0
    score_list = []
    score_list = list(map(int, input().split()))
    for j,score in enumerate(score_list):
        if(j!=0):
            sum += score
    avg = sum / score_list[0]    
    for i in score_list[1:]:
        if i > avg :
            count += 1
    per = count / score_list[0] * 100
    print(f"{per:.3f}%")
