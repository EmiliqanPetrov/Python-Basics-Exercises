command = input()
money_needed = float(input())
money = 0

while command != "End":
    destination = command
    while money_needed > money:
        curr_money = float(input())
        money += curr_money
    money = 0
    print(f"Going to {destination}!")
    command = input()
    if command == "End":
        break
    money_needed = float(input())

