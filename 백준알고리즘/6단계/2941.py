word = input()
croatia_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia_list:
    word = word.replace(i,"!")
print(len(word))