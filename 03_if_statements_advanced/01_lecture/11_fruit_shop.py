fruit = input()
day = input()
quantity = float(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price1 = 2.50
        print(f"{price1 * quantity:.2f}")
    elif fruit == "apple":
        price1 = 1.20
        print(f"{price1 * quantity:.2f}")
    elif fruit == "orange":
        price1 = 0.85
        print(f"{price1 * quantity:.2f}")
    elif fruit == "grapefruit":
        price1 = 1.45
        print(f"{price1 * quantity:.2f}")
    elif fruit == "kiwi":
        price1 = 2.70
        print(f"{price1 * quantity:.2f}")
    elif fruit == "pineapple":
        price1 = 5.50
        print(f"{price1 * quantity:.2f}")
    elif fruit == "grapes":
        price1 = 3.85
        print(f"{price1 * quantity:.2f}")
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price1 = 2.70
        print(f"{price1 * quantity:.2f}")
    elif fruit == "apple":
        price1 = 1.25
        print(f"{price1 * quantity:.2f}")
    elif fruit == "orange":
        price1 = 0.90
        print(f"{price1 * quantity:.2f}")
    elif fruit == "grapefruit":
        price1 = 1.60
        print(f"{price1 * quantity:.2f}")
    elif fruit == "kiwi":
        price1 = 3.00
        print(f"{price1 * quantity:.2f}")
    elif fruit == "pineapple":
        price1 = 5.60
        print(f"{price1 * quantity:.2f}")
    elif fruit == "grapes":
        price1 = 4.20
        print(f"{price1 * quantity:.2f}")
    else:
        print("error")
else:
    print("error")
