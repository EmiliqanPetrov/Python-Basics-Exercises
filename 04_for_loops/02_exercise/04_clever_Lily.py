BROTHER_MONEY = 1.00
MONEY_ADD = 10.00

age = int(input())
price_washing_machine = float(input())
price_toy = int(input())

total_money = 0
money_given = 10.00
profit_toys = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        total_money += (money_given - BROTHER_MONEY)
        money_given += MONEY_ADD
    else:
        profit_toys += price_toy

total_money += profit_toys

if total_money >= price_washing_machine:
    print(f"Yes! {total_money - price_washing_machine:.2f}")
else:
    print(f"No! {price_washing_machine - total_money:.2f}")