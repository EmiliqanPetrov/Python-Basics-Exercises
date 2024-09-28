MAXIMUM_FOR_BULGARIA = 100
SUMMER_BULGARIA = 0.30
WINTER_BULGARIA = 0.70

MAXIMUM_FOR_BALKAN = 1000
SUMMER_BALKAN = 0.40
WINTER_BALKAN = 0.80

MINIMUM_FOR_EUROPE = 1000
SUMMER_WINTER_EUROPE = 0.90

budget = float(input())
season = input()
price = 0
type_holiday = ""
destination = ""

if season == "summer":
    if budget > MINIMUM_FOR_EUROPE:
        type_holiday = "Hotel"
        destination = "Europe"
        price = SUMMER_WINTER_EUROPE * budget
    elif budget <= MAXIMUM_FOR_BULGARIA:
        type_holiday = "Camp"
        destination = "Bulgaria"
        price = SUMMER_BULGARIA * budget
    else:
        type_holiday = "Camp"
        destination = "Balkans"
        price = SUMMER_BALKAN * budget
else:
    if budget > MINIMUM_FOR_EUROPE:
        type_holiday = "Hotel"
        destination = "Europe"
        price = SUMMER_WINTER_EUROPE * budget
    elif budget <= MAXIMUM_FOR_BULGARIA:
        type_holiday = "Hotel"
        destination = "Bulgaria"
        price = WINTER_BULGARIA * budget
    else:
        type_holiday = "Hotel"
        destination = "Balkans"
        price = WINTER_BALKAN * budget

print(f"Somewhere in {destination}")
print(f"{type_holiday} - {price:.2f}")