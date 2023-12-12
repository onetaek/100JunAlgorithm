N = int(input())
big_count_list = []
for i in range(N):
    big_count_list.append(0)
peoInList = []
for _ in range(N):
    tempList = list(map(int,input().split()))
    peoInList.append(tempList)
for i in range(len(peoInList)):
    for j in range(len(peoInList)):
        if i == j:
            continue;
        if peoInList[i][0] < peoInList[j][0] and peoInList[i][1] < peoInList[j][1]:
            big_count_list[i] += 1
for i in big_count_list:
    print(i+1,end=' ')