PERCENT_EXPENSES = 0.05

count_juniors = int(input())
count_seniors = int(input())
category_race = input()

competitors = count_juniors + count_seniors

discount = 0
expenses = 0
charity_money = 0

if category_race == "trail":
    tax_juniors = count_juniors * 5.50
    tax_seniors = count_seniors * 7.00

    full_tax = tax_juniors + tax_seniors
    expenses = full_tax * PERCENT_EXPENSES

    charity_money = full_tax - expenses
elif category_race == "cross-country":
    tax_juniors = count_juniors * 8.00
    tax_seniors = count_seniors * 9.50

    full_tax = tax_juniors + tax_seniors

    if competitors >= 50:
        discount = 0.25

    full_tax -= full_tax * discount
    expenses = full_tax * PERCENT_EXPENSES

    charity_money = full_tax - expenses
elif category_race == "downhill":
    tax_juniors = count_juniors * 12.25
    tax_seniors = count_seniors * 13.75

    full_tax = tax_juniors + tax_seniors
    expenses = full_tax * PERCENT_EXPENSES

    charity_money = full_tax - expenses
elif category_race == "road":
    tax_juniors = count_juniors * 20.00
    tax_seniors = count_seniors * 21.50

    full_tax = tax_juniors + tax_seniors
    expenses = full_tax * PERCENT_EXPENSES

    charity_money = full_tax - expenses

print(f"{charity_money:.2f}")
