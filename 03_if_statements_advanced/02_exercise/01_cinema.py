PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

type_projection = input()
rows = int(input())
columns = int(input())

seats = rows * columns
income = 0

if type_projection == "Premiere":
    income = PREMIERE * seats
elif type_projection == "Normal":
    income = NORMAL * seats
elif type_projection == "Discount":
    income = DISCOUNT * seats

print(f"{income:.2f}")