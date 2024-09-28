product = input()
city = input()
quantity = float(input())

if city == "Sofia":
    if product == "coffee":
        price1 = 0.50
    elif product == "water":
        price1 = 0.80
    elif product == "beer":
        price1 = 1.20
    elif product == "sweets":
        price1 = 1.45
    else:
        price1 = 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price1 = 0.40
    elif product == "water":
        price1 = 0.70
    elif product == "beer":
        price1 = 1.15
    elif product == "sweets":
        price1 = 1.30
    else:
        price1 = 1.50
else:
    if product == "coffee":
        price1 = 0.45
    elif product == "water":
        price1 = 0.70
    elif product == "beer":
        price1 = 1.10
    elif product == "sweets":
        price1 = 1.35
    else:
        price1 = 1.55

price = price1 * quantity

print(price)
