user_input = input()

total_money = 0

while user_input != "NoMoreMoney":
    increase = float(user_input)
    if increase < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {increase:.2f}")
    total_money += increase
    user_input = input()

print(f"Total: {total_money:.2f}")