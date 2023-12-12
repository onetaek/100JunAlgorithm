import sys
sys.stdin = open("input.txt","r")
N = int(input())

def append_str(string,list):
    return string + list[0] * int(list[1])

for test_case in range(1,N+1):
    print(f"#{test_case}")
    cnt = int(input())
    my_board = []
    my_list_to_str = ""
    for _ in range(cnt):
        temp_list = list(input().split())
        my_board.append(temp_list)
    for my_list in my_board:
        my_list_to_str = append_str(my_list_to_str,my_list)

    
    cnt = 0
    for i in my_list_to_str:
        cnt += 1
        print(i,end="")
        if cnt%10 == 0:
            print()
    print()
        

    
    
        


    