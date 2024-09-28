money = float(input())

coins = 0
coins_values = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

for i in coins_values:
    if money // i > 0:
        coins += money // i
        money -= money // i * i
        money = round(money, 2)

print(f"{coins:.0f}")