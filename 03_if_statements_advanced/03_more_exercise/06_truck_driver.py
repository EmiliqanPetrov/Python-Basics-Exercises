TAX = 0.1

season = input()
km_per_month = float(input())

income_per_km = 0

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5_000:
        income_per_km = 0.75
    elif km_per_month <= 10_000:
        income_per_km = 0.95
    else:
        income_per_km = 1.45
elif season == "Summer":
    if km_per_month <= 5_000:
        income_per_km = 0.90
    elif km_per_month <= 10_000:
        income_per_km = 1.10
    else:
        income_per_km = 1.45
else:
    if km_per_month <= 5_000:
        income_per_km = 1.05
    elif km_per_month <= 10_000:
        income_per_km = 1.25
    else:
        income_per_km = 1.45

full_income_no_tax = income_per_km * km_per_month
full_income_with_tax = full_income_no_tax - full_income_no_tax * TAX
full_income_with_tax *= 4

print(f"{full_income_with_tax:.2f}")
    