SPRING = 3_000
SUMMER_AUTUMN = 4_200
WINTER = 2_600

budget = int(input())
season = input()
people = int(input())
discount = 0

if season == "Spring":
    price_rent = SPRING
    if people <= 6:
        price_rent -= (price_rent * 0.10)
    elif people <= 11:
        price_rent -= (price_rent * 0.15)
    elif people > 12:
        price_rent -= (price_rent * 0.25)
elif season == "Summer" or season == "Autumn":
    price_rent = SUMMER_AUTUMN
    if people <= 6:
        price_rent -= (price_rent * 0.10)
    elif people <= 11:
        price_rent -= (price_rent * 0.15)
    elif people > 12:
        price_rent -= (price_rent * 0.25)
else:
    price_rent = WINTER
    if people <= 6:
        price_rent -= (price_rent * 0.10)
    elif people <= 11:
        price_rent -= (price_rent * 0.15)
    elif people > 12:
        price_rent -= (price_rent * 0.25)

if season != "Autumn":
    if people % 2 == 0:
        discount = 0.05

price = price_rent - price_rent * discount

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
