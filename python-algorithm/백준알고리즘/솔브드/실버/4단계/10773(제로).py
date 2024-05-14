# https://www.acmicpc.net/problem/10773

import sys

sys.stdin = open("input.txt", "r")
N = int(input())
numbers = [int(input()) for _ in range(N)]
queue = []
"""
<코딩하기전 머리속으로 로직 정리>
- for문을 돌면서 numbers의 각 원소를 더한다.
- 0을 만나면 이전 index의 값을 빼주면 될 것 같다.

<코딩하다 로직 수정>
- 연속으로 0을 만날 경우 위 조건으로 처리못함
- 스택을 사용하는게 적절하겠구만
"""
for i in range(len(numbers)):
    number = numbers[i]
    if (number == 0):
        queue.pop()
    else:
        queue.append(number)

print(sum(queue))

