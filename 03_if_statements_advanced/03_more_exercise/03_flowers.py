PERCENT_UP_HOLIDAYS = 0.15

count_chrysanthemums = int(input())
count_roses = int(input())
count_hyacinths = int(input())
season = input()
is_holiday = input()

count_all_flowers = count_chrysanthemums + count_roses + count_hyacinths
discount = 0
price = 0

if season == "Spring":
    price_chrysanthemums = count_chrysanthemums * 2.00
    price_roses = count_roses * 4.10
    price_hyacinths = count_hyacinths * 2.50
    price_all_flowers = price_chrysanthemums + price_roses + price_hyacinths

    if is_holiday == "Y":
        price_all_flowers += price_all_flowers * PERCENT_UP_HOLIDAYS

    if count_all_flowers > 20:
        discount = 0.2
        price_all_flowers -= price_all_flowers * discount
    if count_hyacinths > 7:
        discount = 0.05
        price_all_flowers -= price_all_flowers * discount

    price = price_all_flowers
elif season == "Summer":
    price_chrysanthemums = count_chrysanthemums * 2.00
    price_roses = count_roses * 4.10
    price_hyacinths = count_hyacinths * 2.50
    price_all_flowers = price_chrysanthemums + price_roses + price_hyacinths

    if is_holiday == "Y":
        price_all_flowers += price_all_flowers * PERCENT_UP_HOLIDAYS

    if count_all_flowers > 20:
        discount += 0.2

    price = price_all_flowers - price_all_flowers * discount
elif season == "Autumn":
    price_chrysanthemums = count_chrysanthemums * 3.75
    price_roses = count_roses * 4.50
    price_hyacinths = count_hyacinths * 4.15
    price_all_flowers = price_chrysanthemums + price_roses + price_hyacinths

    if is_holiday == "Y":
        price_all_flowers += price_all_flowers * PERCENT_UP_HOLIDAYS

    if count_all_flowers > 20:
        discount += 0.2

    price = price_all_flowers - price_all_flowers * discount
elif season == "Winter":
    price_chrysanthemums = count_chrysanthemums * 3.75
    price_roses = count_roses * 4.50
    price_hyacinths = count_hyacinths * 4.15
    price_all_flowers = price_chrysanthemums + price_roses + price_hyacinths

    if is_holiday == "Y":
        price_all_flowers += price_all_flowers * PERCENT_UP_HOLIDAYS

    if count_roses >= 10:
        discount = 0.1
        price_all_flowers -= price_all_flowers * discount
    if count_all_flowers > 20:
        discount = 0.2
        price_all_flowers -= price_all_flowers * discount

    price = price_all_flowers

print(f"{price + 2:.2f}")
