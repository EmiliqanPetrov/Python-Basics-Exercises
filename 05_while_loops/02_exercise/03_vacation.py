money_needed = float(input())
money_owned = float(input())

days_count = 0
spend_days = 0

while money_owned < money_needed and spend_days < 5:
    command = input()
    money = float(input())
    days_count += 1
    
    if command == "spend":
        spend_days += 1
        money_owned -= money

        if money_owned < 0:
            money_owned = 0
    else:
        spend_days = 0
        money_owned += money

if spend_days == 5:
    print(f"You can't save the money.\n{days_count}")

if money_owned >= money_needed:
    print(f"You saved the money for {days_count} days.")

