price1_kg = float(input())
price2_kg = float(input())
kg3 = float(input())
kg4 = float(input())
kg5 = int(input())
price5_kg = 7.50

price3_kg = price1_kg + price1_kg * 0.60
sum3 = kg3 * price3_kg

price4_kg = price2_kg + price2_kg * 0.80
sum4 = kg4 * price4_kg

sum5 = kg5 * price5_kg

full_sum = sum3 + sum4 + sum5

print(f"{full_sum:.2f}")



