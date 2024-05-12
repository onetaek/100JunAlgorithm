import sys

sys.stdin = open("input.txt", "r")
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

"""
<코딩하기전 로직 정리>

1. 오름차순으로 있는 list를 맨 뒤의 값(큰 값)을 비교 대상으로 정한다.
2. K - (비교대상)의 값이 양수, 음수, 0 각각의 값에 따라 다르게 분기를 태운다.
3. 0이 되면 종료하고 2번과정에서 계산된 count 값을 출력한다.
"""

index = len(coins) - 1 
count = 0
calcMoney = K
while calcMoney > 0:
    if coins[index] <= calcMoney:
        count += calcMoney // coins[index]
        calcMoney %= coins[index]
    index -= 1

print(count)

sys.stdin.close()