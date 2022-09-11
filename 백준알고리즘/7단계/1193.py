line = 1
range = 1
N = int(input())
while(N > range):
    line += 1
    range += line
th = range - N 

if line % 2 == 0:
    print(f"{line - th}/{1 + th}")
elif line % 2 ==1:
    print(f"{1 + th}/{line - th}")