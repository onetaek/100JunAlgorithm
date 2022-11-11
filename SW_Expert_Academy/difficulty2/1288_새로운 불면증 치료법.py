import sys
sys.stdin = open('input.txt','r')
N = int(input())

for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    str_num = input()
    first_str_num = str_num

    check_list = ['0','1','2','3','4','5','6','7','8','9']
    cnt = 0
    K = 1

    while check_list != []:
        str_num = str( int(first_str_num) * K )
        for str_n in str_num:
            for check in check_list:
                if check == str_n:
                    check_list.remove(str_n)
        K += 1
        cnt += 1
    print(str_num)
    