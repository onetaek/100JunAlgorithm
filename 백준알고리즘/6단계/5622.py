from distutils.log import WARN


alphbet_list = ["","","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

word = input()
time = 0

for i,alphbet_set in enumerate(alphbet_list):
    for j in word:
        if alphbet_set.find(j) != -1:
            time += i
print(time)