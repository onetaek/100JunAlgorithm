N = int(input())

run = True
cycle = 1
room = 1

while(run):
    if room >= N:
        break
    room += (6 * cycle)
    cycle += 1

print(cycle)