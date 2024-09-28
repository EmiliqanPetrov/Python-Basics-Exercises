budget = float(input())
season = input()

place = ""
stay = ""
price = 0

if budget <= 1000:
    stay = "Camp"

    if season == "Summer":
        price = budget * 0.65
        place = "Alaska"
    else:
        price = budget * 0.45
        place = "Morocco"
elif budget <= 3000:
    stay = "Hut"

    if season == "Summer":
        price = budget * 0.8
        place = "Alaska"
    else:
        price = budget * 0.6
        place = "Morocco"
else:
    stay = "Hotel"

    if season == "Summer":
        price = budget * 0.9
        place = "Alaska"
    else:
        price = budget * 0.9
        place = "Morocco"

print(f"{place} - {stay} - {price:.2f}")