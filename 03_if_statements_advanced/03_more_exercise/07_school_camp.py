season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())

if group_type == "boys" or group_type == "girls":
    if season == "Winter":
        price_per_student = 9.60
    elif season == "Spring":
        price_per_student = 7.20
    else:
        price_per_student = 15.00
else:
    if season == "Winter":
        price_per_student = 10.00
    elif season == "Spring":
        price_per_student = 9.50
    else:
        price_per_student = 20.00

price_nights = count_nights * count_students * price_per_student

if count_students >= 50:
    discount = 0.5
elif 20 <= count_students < 50:
    discount = 0.15
elif 10 <= count_students < 20:
    discount = 0.05
else:
    discount = 0

price = price_nights - price_nights * discount

if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    else:
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    else:
        sport = "Football"
else:
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    else:
        sport = "Swimming"

print(f"{sport} {price:.2f} lv.")
