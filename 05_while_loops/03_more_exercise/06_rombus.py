n = int(input())

for row in range(2, n + 1):
    print(f"{(n - row) * ' '}{(row - 1) * ' *'}")

for row2 in range(n, 0, -1):
    print(f"{(n - row2) * ' '}{row2 * '* '}")