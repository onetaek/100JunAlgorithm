N = int(input())
test_num = 666
i = 1

while i < N+1:
    str_test_num = str(test_num)
    if str_test_num.find('666') >= 0 or str_test_num.find('6666') >= 0:
        pass
    else:
        i -= 1
    test_num += 1
    i+=1
test_num -= 1
print(test_num)