import sys
sys.stdin = open("input.txt","r")
N = int(input())
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="")
    # Base64변환순서
    #1. 2진수로 변환 -> 부호값함쳐서 8자리차지
    #2. 8자리씩있는걸 -> 6자릿씩나눔
    #3. 6자리의 2진수를 10진수로 바꿈
    #4. Base64를 참조하여 문자로 변환
    #우리가 해야할 것은 이것을 거꾸로해야함
    #4개의 Base64문자는 3개의 문자로 바뀐다.

    def strTo2(num):

        return 0

    Base64 ={}
    for i in range(0,26):
        Base64[i] = chr(i+65)
    for i in range(26,52):
        Base64[i] = chr(i+71)
    for i in range(52,62):
        Base64[i] = str(i-52)
    Base64[62] = "+"
    Base64[63] = "/"
    str_64 = input()
    reverse_Base64= dict(map(reversed,Base64.items()))
    strToNum = []
    NumTo2 = []
    for i in range(len(str_64)):   
        strToNum.append(reverse_Base64[str_64[i]])
    for num in range(len(strToNum)):
        NumTo2.append(format(num, 'b'))
    print(strToNum)
    print(NumTo2)