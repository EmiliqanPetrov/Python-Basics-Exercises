import math

MAGNOLIA = 3.25
HYACINTH = 4.00
ROSE = 3.50
CACTUS = 8.00

count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cacti = int(input())
price_present = float(input())

price_magnolias = count_magnolias * MAGNOLIA
price_hyacinths = count_hyacinths * HYACINTH
price_roses = count_roses * ROSE
price_cacti = count_cacti * CACTUS

price_flowers = price_magnolias + price_hyacinths + price_roses + price_cacti

income = 0.95 * price_flowers

if income >= price_present:
    leftover = income - price_present
    print(f"She is left with {math.floor(leftover)} leva." )
else:
    more_needed = price_present - income
    print(f"She will have to borrow {math.ceil(more_needed)} leva.")


