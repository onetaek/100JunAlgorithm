def solution(money):
    money = str(money)
    print(money)
    count = 0
    for i in range(len(money)):
        print('!',len(money) - 1)
        if i == len(money) - 1:
            print(int(money[i]))
            count += int(money[i])
        else:
            if int(money[i]) >= 5:
                print('!',int(money[i])-4)
                count += int(money[i])-4
            else:
                print(int(money[i]))
                count += int(money[i])
    return count

print(solution(12345))
