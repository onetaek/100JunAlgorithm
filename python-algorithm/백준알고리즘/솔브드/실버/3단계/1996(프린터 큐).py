# https://www.acmicpc.net/problem/1966

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    result = 1
    while data:
        # 제일 왼쪽의 data 가 최우선 순위가 아닐경우
        if data[0] < max(data):
            data.append(data.pop(0))
        # 제일 왼쪽의 data 가 최우선 순위일 경우
        else:
            # m 인덱스를 만났을 경우
            if m == 0: break

            # 제일 왼쪽의 data를 버리고 우선순위를 +1 한다.
            data.pop(0)
            result += 1

        # 데이터를 pop 했으니 m 값도 같이 이동 시켜주기 위함
        m = m - 1 if m > 0 else len(data) - 1

    print(result)
