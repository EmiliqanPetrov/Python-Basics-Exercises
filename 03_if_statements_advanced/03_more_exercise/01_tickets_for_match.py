VIP_TICKETS = 499.99
NORMAL_TICKETS = 249.99

budget = float(input())
category_tickets = input()
count_people = int(input())

transport_percent = 0
price_tickets = 0

if 0 <= count_people <= 4:
    transport_percent = 0.75
elif 5 <= count_people <= 9:
    transport_percent = 0.6
elif 10 <= count_people <= 24:
    transport_percent = 0.5
elif 25 <= count_people <= 49:
    transport_percent = 0.4
else:
    transport_percent = 0.25

transport_price = budget * transport_percent

money_for_tickets = budget - transport_price

if category_tickets == "VIP":
    price_tickets = VIP_TICKETS * count_people
elif category_tickets == "Normal":
    price_tickets = NORMAL_TICKETS * count_people

if money_for_tickets >= price_tickets:
    print(f"Yes! You have {money_for_tickets - price_tickets:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_tickets - money_for_tickets:.2f} leva.")
