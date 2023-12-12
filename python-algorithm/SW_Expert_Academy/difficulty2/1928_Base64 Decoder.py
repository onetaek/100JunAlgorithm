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

    def twoToLen8(two):
        add_cnt = 6 - len(two)
        for _ in range(add_cnt):
            two = "0"+two
        return two
    
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
    tweToLen6 = []
    len6ToLen8 = []
    strFrom2 = ""
    twoTo10 = []
    asciiToStr = []
    answer = ""
    #딕셔너리에 저장된 값을 value를 통해 key를 찾기위해 뒤집는다.
    #뒤집고나서  Base64표를 참조하여 문자에 해당하는 숫자를 찾는다.
    for i in range(len(str_64)):   
        strToNum.append(reverse_Base64[str_64[i]])
    # 숫자를 2진수로 변환
    for num in strToNum:
        NumTo2.append(format(num, 'b'))
    # 2진수여서 110이런식으로 나오는데 자릿수를 모두 6자리로 맞춰준다.
    for num in NumTo2:
        tweToLen6.append(twoToLen8(num))
    # 6자리를 하나의 문자열로 붙힌다
    for stri in tweToLen6:
        strFrom2 += stri
    # 붙힌 문자열을 다시 8자리로 자른다.
    while strFrom2 != "":
        len6ToLen8.append(strFrom2[:8])
        strFrom2 = strFrom2[8:]
    # 8자리로 자른 2진수를 10진수(ascii)로 바꾼다.
    for two in len6ToLen8:
        twoTo10.append(int(two,2))
    # ascii를 문자로 변환한다.
    for ascii in twoTo10:
        asciiToStr.append(chr(ascii))
    # 문자라 list형태로 있어서 하나의 string으로 만든다.
    for st in asciiToStr:
        answer += st
    print(answer)