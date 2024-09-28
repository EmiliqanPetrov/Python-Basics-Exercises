NYLON_ONE = 1.50
PAINT_ONE_LITER = 14.50
PAINT_THINNER_ONE_LITER = 5.00
BAG_ONE = 0.40

count_nylon = int(input())
count_paint = int(input())
count_paint_thinner = int(input())
work_hours = int(input())

price_nylon = (count_nylon + 2) * NYLON_ONE
price_paint = (count_paint + (count_paint * (10 / 100))) * PAINT_ONE_LITER
price_paint_thinner = count_paint_thinner * PAINT_THINNER_ONE_LITER
price_bag = BAG_ONE

price_materials = price_bag + price_paint_thinner + price_paint + price_nylon
price_workers = (price_materials * (30 / 100) * work_hours)

final_price = price_workers + price_materials

print(final_price)
