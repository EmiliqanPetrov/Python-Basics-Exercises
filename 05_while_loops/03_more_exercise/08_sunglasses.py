import math

n = int(input())

if n % 2 == 0:
    holder = (n - 2) / 2
else:
    holder = math.ceil((n - 2) / 2)

print(f"{(2 * n) * '*'}{n * ' '}{(2 * n) * '*'}")

for i in range(1, n - 2 + 1):
    if i == holder:
        print(f"*{(2 * n - 2) * '/'}*{n * '|'}*{(2 * n - 2) * '/'}*")
    else:
        print(f"*{(2 * n - 2) * '/'}*{n * ' '}*{(2 * n - 2) * '/'}*")

print(f"{(2 * n) * '*'}{n * ' '}{(2 * n) * '*'}")