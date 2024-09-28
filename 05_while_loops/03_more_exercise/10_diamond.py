import math

n = int(input())

if n % 2 == 0:
    side_underscores = math.floor((n - 1) / 2)
    for _ in range(round(n / 2)):
        print(f"{side_underscores * '-'}*{round(n - (side_underscores * 2 + 2)) * '-'}*{side_underscores * '-'}")
        side_underscores -= 1
    side_underscores += 2
    for __ in range(round(n / 2 - 1)):
        print(f"{side_underscores * '-'}*{round(n - (side_underscores * 2 + 2)) * '-'}*{side_underscores * '-'}")
        side_underscores += 1
else:
    side_underscores = math.floor(n / 2 - 1)
    print(f"{(side_underscores + 1) * '-'}*{(side_underscores + 1) * '-'}")
    for _ in range(math.floor(n / 2)):
        print(f"{side_underscores * '-'}*{round(n - (side_underscores * 2 + 2)) * '-'}*{side_underscores * '-'}")
        side_underscores -= 1
    side_underscores += 2
    for _ in range(math.floor(n / 2 - 1)):
        print(f"{side_underscores * '-'}*{round(n - (side_underscores * 2 + 2)) * '-'}*{side_underscores * '-'}")
        side_underscores += 1
    if n != 1:
        side_underscores = math.floor(n / 2 - 1)
        print(f"{(side_underscores + 1) * '-'}*{(side_underscores + 1) * '-'}")
