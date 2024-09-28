START_TAX_TAXI = 0.70
DAY_TAX_TAXI_KM = 0.79
NIGHT_TAX_TAXI_KM = 0.90
DAY_NIGHT_TAX_BUS_KM = 0.09
DAY_NIGHT_TAX_TRAIN_KM = 0.06

km_count = int(input())
day_night = str(input())

if day_night == "day":
    if km_count < 20:
        price = START_TAX_TAXI + DAY_TAX_TAXI_KM * km_count
        print(f"{price:.2f}")
    elif km_count >= 100:
        price1 = DAY_NIGHT_TAX_TRAIN_KM * km_count
        price2 = DAY_NIGHT_TAX_BUS_KM * km_count
        print(f"{price1:.2f}")
    else:
        price1 = DAY_NIGHT_TAX_BUS_KM * km_count
        price2 = DAY_NIGHT_TAX_TRAIN_KM * km_count
        price3 = START_TAX_TAXI + DAY_TAX_TAXI_KM * km_count
        if price1 >= price2:
            print(f"{price1:.2f}")
        else:
            print(f"{price2:.2f}")

elif day_night == "night":
    if km_count < 20:
        price = START_TAX_TAXI + NIGHT_TAX_TAXI_KM * km_count
        print(f"{price:.2f}")
    elif km_count >= 100:
        price = DAY_NIGHT_TAX_TRAIN_KM * km_count
        print(f"{price:.2f}")
    else:
        price1 = DAY_NIGHT_TAX_BUS_KM * km_count
        price2 = DAY_NIGHT_TAX_TRAIN_KM * km_count
        if price1 >= price2:
            print(f"{price1:.2f}")
        else:
            print(f"{price2:.2f}")


