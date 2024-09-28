n = int(input())

numbers = []

for i in range(1, n + 1):
    if i < 10:
        if n / i == n // i:
            numbers.append(i)

for x1 in numbers:
    for x2 in numbers:
        for x3 in numbers:
            for x4 in numbers:
                print(f"{x1}{x2}{x3}{x4}", end=' ')