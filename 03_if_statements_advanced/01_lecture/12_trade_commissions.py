city = input()
sum = float(input())

percent = 0

if city == "Sofia":
    if 0 <= sum <= 500:
        percent = 0.05
    elif 500 < sum <= 1000:
        percent = 0.07
    elif 1000 < sum <= 10_000:
        percent = 0.08
    elif sum > 10_000:
        percent = 0.12
    else:
        print("error")
        exit()
elif city == "Varna":
    if 0 <= sum <= 500:
        percent = 0.045
    elif 500 < sum <= 1000:
        percent = 0.075
    elif 1000 < sum <= 10_000:
        percent = 0.10
    elif sum > 10_000:
        percent = 0.13
    else:
        print("error")
        exit()
elif city == "Plovdiv":
    if 0 <= sum <= 500:
        percent = 0.055
    elif 500 < sum <= 1000:
        percent = 0.08
    elif 1000 < sum <= 10_000:
        percent = 0.12
    elif sum > 10_000:
        percent = 0.145
    else:
        print("error")
        exit()
else:
    print("error")
    exit()

money = percent * sum

print(f"{money:.2f}")
