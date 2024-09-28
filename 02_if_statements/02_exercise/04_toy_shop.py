PUZZLE = 2.60
DOLL = 3.00
TEDDI_BEAR = 4.10
MINION = 8.20
TRUCK = 2.00

holiday = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_teddi_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_puzzles = PUZZLE * count_puzzles
price_dolls = DOLL * count_dolls
price_teddi_bears = TEDDI_BEAR * count_teddi_bears
price_minions = MINION * count_minions
price_trucks = TRUCK * count_trucks

price_toys = (price_puzzles + price_dolls + price_teddi_bears + price_minions + price_trucks)
count_toys = count_puzzles + count_dolls + count_teddi_bears + count_minions + count_trucks

if count_toys >= 50:
    full_price = price_toys - (price_toys * 0.25)
else:
    full_price = price_toys

rent = 0.1 * full_price
income = full_price - rent

if income >= holiday:
    leftover = income - holiday
    print(f"Yes! {leftover:.2f} lv left.")
else:
    more_needed = holiday - income
    print(f"Not enough money! {more_needed:.2f} lv needed.")