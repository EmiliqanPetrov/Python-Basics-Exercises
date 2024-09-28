ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00
POSITIVE_REVIEW_PERCENT = 0.25
NEGATIVE_REVIEW_PERCENT = 0.1

days = int(input())
type_room = input()
review = input()

sleepovers = days - 1
discount = 0
price = 0

if type_room == "room for one person":
    price = sleepovers * ROOM_FOR_ONE_PERSON

    if review == "positive":
        price += price * POSITIVE_REVIEW_PERCENT
    elif review == "negative":
        price -= price * NEGATIVE_REVIEW_PERCENT
elif type_room == "apartment":
    price = sleepovers * APARTMENT

    if sleepovers < 10:
        discount = 0.3
    elif sleepovers <= 15:
        discount = 0.35
    else:
        discount = 0.5

    price -=  price * discount

    if review == "positive":
        price += price * POSITIVE_REVIEW_PERCENT
    elif review == "negative":
        price -= price * NEGATIVE_REVIEW_PERCENT
elif type_room == "president apartment":
    price = sleepovers * PRESIDENT_APARTMENT

    if sleepovers < 10:
        discount = 0.1
    elif sleepovers <= 15:
        discount = 0.15
    else:
        discount = 0.2

    price -= price * discount

    if review == "positive":
        price += price * POSITIVE_REVIEW_PERCENT
    elif review == "negative":
        price -= price * NEGATIVE_REVIEW_PERCENT

print(f"{price:.2f}")
