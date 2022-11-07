# import sys
# sys.stdin = open('input.txt','r')
N = int(input())

def show(num_list):
    for n in num_list:
        print(n,end=" ")
    print()
    return 0

def pascal(num,cnt,num_list):
    if cnt == num:
        return 0
    if len(num_list) == 1:
        show(num_list)
        num_list.append(1)
        cnt +=1
        return pascal(num,cnt,num_list)
    elif len(num_list) ==2 :
        show(num_list)
        next_list = []
        next_list.append(1)
        next_list.append(2)
        next_list.append(1)
        cnt +=1
        return pascal(num,cnt,next_list)
    else:
        show(num_list)
        next_list =[]
        next_list.append(1)
        for i in range(len(num_list)-1):
            next_list.append(num_list[i]+num_list[i+1])
        next_list.append(1)
        cnt +=1
        return pascal(num,cnt,next_list)
        # print(temp_list)

for test_case in range(1,N+1):
    num = int(input())
    print(f"#{test_case}")
    num_list = [1]
    cnt = 0
    pascal(num,cnt,num_list)

