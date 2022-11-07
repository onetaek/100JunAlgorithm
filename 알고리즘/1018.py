a,b = map(int,input().split())
inputList = []
#2차원 배열의 형태로 받아준다.
for _ in range(a):
    inputList.append(input())
    
#i,j위치를 받아서 그점으로 부터 8X8의 크기의 체크판을 만든다.
def makeChessList(i,j,inputList):
    temp=[]
    for k in range(i,i+8):
        temp.append(inputList[k][j:j+8])
    return temp

#chess판중 하나의 줄중에서 바꾸어야할 갯수를 구한다.
def diff_count(chessStr,lastColor):
    Color = lastColor
    cnt = 0
    for chess in chessStr:
        if chess != Color:
            cnt += 1
        Color = "B" if Color == "W" else "W"
    return cnt

#W으로 시작할 때 B로 시작할때 2가지 경우의 수가 있다.
def chess8x8_sum(chessList):
    ColorList = ["W","B"]
    min_sum = -1
    for Color in ColorList:
        temp_sum = 0
        for chessStr in chessList:
            temp_sum += diff_count(chessStr,Color)
            Color = "W" if Color == "B" else "B"

        if min_sum == -1:
            min_sum = temp_sum
        elif temp_sum < min_sum:
            min_sum = temp_sum
    return min_sum

allChessList = []

#처음받은 입력값을 8X8의 크기로 자른 모든 경우의수를 구해서
#2차원 배열로 만든다.
for i in range(len(inputList)-7):
    for j in range(len(inputList[0])-7):
        allChessList.append(makeChessList(i,j,inputList))

all_min_sum = -1

for chessList in allChessList:
    #8X8의 체스판하나의 교체할 chess점의 최소갯수를 구한다.
    #판하나당 2개의 경우의 수가 나온다.
    temp_sum = chess8x8_sum(chessList)
    if all_min_sum == -1:
        all_min_sum = temp_sum
    elif temp_sum < all_min_sum:
        all_min_sum = temp_sum

print(all_min_sum)

