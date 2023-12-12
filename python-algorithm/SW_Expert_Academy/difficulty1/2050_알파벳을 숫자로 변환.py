import sys
sys.stdin = open('input.txt','r')

alpha = input()
for i in alpha:
    print(ord(i)-64,end=' ')