import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")
    date = input()
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:])
    if month == 2:
        if day < 1 or day > 28:
            print(-1)
        else:
            print(f"{year:04d}/{month:02d}/{day:02d}")
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            print(-1)
        else:
            print(f"{year:04d}/{month:02d}/{day:02d}")

    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            print(-1)
        else:
            print(f"{year:04d}/{month:02d}/{day:02d}")

    else:
        print(-1)
