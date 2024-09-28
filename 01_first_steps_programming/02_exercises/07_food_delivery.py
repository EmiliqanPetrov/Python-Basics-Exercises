CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15

count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegetarian_menus = int(input())

price_chicken_menus = count_chicken_menus * CHICKEN_MENU
price_fish_menus = count_fish_menus * FISH_MENU
price_vegetarian_menus = count_vegetarian_menus * VEGETARIAN_MENU

price_menus = price_vegetarian_menus + price_fish_menus + price_chicken_menus
price_desert = price_menus * (20 / 100)
price_delivery = 2.50

final_price = price_desert + price_menus + price_delivery

print(f"{final_price}")