count_pens = int(input())
count_markers = int(input())
liters_BC = int(input())
percent_disc = int(input()) / 100

price_pens = count_pens * 5.80
price_markers = count_markers * 7.20
price_BC = liters_BC * 1.20

full_price = price_BC + price_pens + price_markers

final_price = full_price - (full_price * percent_disc)

print(final_price)