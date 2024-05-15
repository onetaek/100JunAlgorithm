from collections import deque

def lastCard(N):
    # N개의 카드를 deque에 담습니다.
    queue = deque(range(1, N + 1))

    # 큐가 한 장 남을 때까지 반복합니다.
    while len(queue) > 1:
        # 제일 위에 있는 카드를 버립니다.
        queue.popleft()
        # 제일 위에 있는 카드를 제일 아래로 옮깁니다.
        queue.append(queue.popleft())
    
    # 마지막에 남은 카드 반환
    return queue[0]

N = int(input())

print(lastCard(N))