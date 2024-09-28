ROSE = 5.00
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3.00
GLADIOLUS = 2.50

type_flowers = input()
count_flowers = int(input())
budget = int(input())
discount = 0
price = 0

if type_flowers == "Roses":
    price = ROSE * count_flowers
    if count_flowers > 80:
        discount = 0.10
    price -= price * discount
elif type_flowers == "Dahlias":
    price = DAHLIA * count_flowers
    if count_flowers > 90:
        discount = 0.15
    price -= price * discount
elif type_flowers == "Tulips":
    price = TULIP * count_flowers
    if count_flowers > 80:
        discount = 0.15
    price -= price * discount
elif type_flowers == "Narcissus":
    price = NARCISSUS * count_flowers
    if count_flowers < 90:
        discount = 0.15
    price += price * discount
elif type_flowers == "Gladiolus":
    price = GLADIOLUS * count_flowers
    if count_flowers < 80:
        discount = 0.20
    price += price * discount

if budget >= price:
    leftover = budget - price
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {leftover:.2f} leva left.")
else:
    more_needed = price - budget
    print(f"Not enough money, you need {more_needed:.2f} leva more.")