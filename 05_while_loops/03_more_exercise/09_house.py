import math

n = int(input())

if n % 2 == 0:
    stars = 2
    underscores = math.floor(n / 2 - 1)
    for _ in range(math.floor((n + 1) / 2)):
        print(f"{underscores * '-'}{stars * '*'}{underscores * '-'}")
        stars += 2
        underscores -= 1
    for __ in range(math.floor(n / 2)):
        print(f"|{(n - 2) * '*'}|")
else:
    stars = 1
    underscores = math.ceil(n / 2 - 1)
    for _ in range(math.floor((n + 1) / 2)):
        print(f"{underscores * '-'}{stars * '*'}{underscores * '-'}")
        stars += 2
        underscores -= 1
    for __ in range(math.floor(n / 2)):
        print(f"|{(n - 2) * '*'}|")