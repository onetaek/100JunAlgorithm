def hanoi(frm, to, n):
    if n == 1:

        print(f'{frm} {to}')
    else:
        empty = 6 - frm - to
        hanoi(frm, empty, n - 1)

        print(f'{frm} {to}')
        hanoi(empty, to, n - 1)


numberOfDisk = int(input())
print(2**numberOfDisk -1)
hanoi(1, 3, numberOfDisk)
