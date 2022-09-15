N, k = map(int,input().split())
score_list = list(map(int,input().split()))

def solve(score_list: list, num: int) -> int:
    return sorted(score_list, reverse =True)[num-1]

print(solve(score_list,k))