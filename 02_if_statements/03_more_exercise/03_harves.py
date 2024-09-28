import math

PERCENT_WINE = 0.4
GRAPES_WINE = 2.5

square_meters = int(input())
grapes_square_meter = float(input())
needed_wine = int(input())
count_workers = int(input())

all_grapes = square_meters * grapes_square_meter
wine = PERCENT_WINE * all_grapes / GRAPES_WINE

if wine >= needed_wine:
    leftover = wine - needed_wine
    per_worker = leftover / count_workers
    print(f"Good harvest this year! Total wine: {wine:.0f} liters.")
    print(f"{math.ceil(leftover)} liters left -> {math.ceil(per_worker)} liters per person.")
else:
    more_needed = needed_wine - wine
    if (more_needed * 10) % 10 == 0 and type(more_needed) == float:
        print(f"It will be a tough winter! More {more_needed:.0f} liters wine needed.")
    else:
        print(f"It will be a tough winter! More {math.floor(more_needed)} liters wine needed.")