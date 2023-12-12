import sys
sys.stdin = open("input.txt", "r")
T = int(input())
num_list = list(map(int,input().split()))
num_list = sorted(num_list)
mid_idx = int(len(num_list)/2)
print(num_list[mid_idx])