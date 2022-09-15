import sys
N = int(sys.stdin.readline())
person_list = []
for _ in range(N):
    person_list.append(list(sys.stdin.readline().split()))

person_list.sort(key=lambda person: int(person[0]))

for i in range(len(person_list)):
    print(person_list[i][0],person_list[i][1])