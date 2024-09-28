EURO_TO_BGN = 1.94

price_kg_vegetable = float(input())
price_kg_fruit = float(input())
amount_kg_vegetables = int(input())
amount_kg_fruits = int(input())

price_vegetables = price_kg_vegetable * amount_kg_vegetables
price_fruits = price_kg_fruit * amount_kg_fruits

full_price_bgn = price_fruits + price_vegetables
full_price_euro = full_price_bgn / EURO_TO_BGN

print(f"{full_price_euro:.2f}")

