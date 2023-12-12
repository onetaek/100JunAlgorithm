import sys
sys.stdin = open("input.txt","r")
T = int(input())
for _ in range(T):
    word_list = list(input()[::-1].split())
    word_list.reverse()
    for word in word_list:
        print(word,end=" ")
    print()