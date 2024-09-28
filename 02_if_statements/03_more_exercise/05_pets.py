import math

KG_TO_G = 1000

days_count = int(input())
food_available_kg = int(input())
dog_day_kg = float(input())
cat_day_kg = float(input())
turtle_day_g = float(input())

turtle_day_kg = turtle_day_g / KG_TO_G

dog_all_kg = dog_day_kg * days_count
cat_all_kg = cat_day_kg * days_count
turtle_all_kg = turtle_day_kg * days_count

all_food_kg = dog_all_kg + cat_all_kg + turtle_all_kg

if food_available_kg >= all_food_kg:
    leftover = food_available_kg - all_food_kg
    print(f"{math.floor(leftover)} kilos of food left.")
else:
    more_needed = all_food_kg - food_available_kg
    print(f"{math.ceil(more_needed)} more kilos of food are needed.")