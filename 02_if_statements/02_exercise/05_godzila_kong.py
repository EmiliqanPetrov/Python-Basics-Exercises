money = float(input())
actors = int(input())
price_clothing_actor = float(input())

price_decor = money * 0.1
price_clothing = actors * price_clothing_actor

if actors > 150:
    price_clothing = price_clothing - (price_clothing * 0.1)
else:
    price_clothing = price_clothing

money_needed = price_clothing + price_decor

if money >= money_needed:
    leftover = money - money_needed
    print(f"Action!")
    print(f"Wingard starts filming with {leftover:.2f} leva left.")
else:
    more_needed = money_needed - money
    print(f"Not enough money!")
    print(f"Wingard needs {more_needed:.2f} leva more.")