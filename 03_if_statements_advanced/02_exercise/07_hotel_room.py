STUDIO_MAY_OCT = 50
STUDIO_JUN_SEP = 75.20
STUDIO_JUL_AUG = 76
APARTMENT_MAY_OCT = 65
APARTMENT_JUN_SEP = 68.70
APARTMENT_JUL_AUG = 77

month = input()
nights = int(input())
discount_studio = 0
discount_apartment = 0
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    if nights > 14:
        discount_studio = 0.3
    elif nights > 7:
        discount_studio = 0.05

    if nights > 14:
        discount_apartment = 0.1

    price_studio = (STUDIO_MAY_OCT * nights) - (STUDIO_MAY_OCT * nights) * discount_studio
    price_apartment = (APARTMENT_MAY_OCT * nights) - (APARTMENT_MAY_OCT * nights) * discount_apartment
elif month == "June" or month == "September":
    if nights > 14:
        discount_studio = 0.2
        discount_apartment = 0.1

    price_studio = (STUDIO_JUN_SEP * nights) - (STUDIO_JUN_SEP * nights) * discount_studio
    price_apartment = (APARTMENT_JUN_SEP * nights) - (APARTMENT_JUN_SEP * nights) * discount_apartment
elif month == "July" or month == "August":
    if nights > 14:
        discount_apartment = 0.1
    price_studio = (STUDIO_JUL_AUG * nights) - (STUDIO_JUL_AUG * nights) * discount_studio
    price_apartment = (APARTMENT_JUL_AUG * nights) - (APARTMENT_JUL_AUG * nights) * discount_apartment

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")