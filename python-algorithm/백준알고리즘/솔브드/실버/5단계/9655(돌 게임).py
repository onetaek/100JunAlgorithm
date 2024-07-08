import sys
sys.stdin = open('input.txt','r')

# n = 1 -> 상근 승
# n = 2 -> 창녕 승
# n = 3 -> 상근 승
# n = 4 -> 창녕 승 (상근이가 1개를 집근 3개를 집근 창녕 승)

n = int(input())
if n % 2 == 0:
    print('CY')
else:
    print('SK')