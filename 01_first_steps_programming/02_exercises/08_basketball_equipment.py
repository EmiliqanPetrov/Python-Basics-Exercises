annual_tax = int(input())

shoes = annual_tax - (annual_tax * (40 / 100))
outfit = shoes - (shoes * (20 / 100))
ball = outfit * (1 / 4)
other = ball * (1 / 5)

price = annual_tax + shoes + outfit + ball + other

print(price)