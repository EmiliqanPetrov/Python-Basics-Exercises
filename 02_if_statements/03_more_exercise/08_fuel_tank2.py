GAS = 0.93
DISCOUNT_GAS = 0.08
GASOLINE = 2.22
DISCOUNT_GASOLINE = 0.18
DIESEL = 2.33
DISCOUNT_DIESEL = 0.12

type_fuel = str(input())
quantity_fuel = float(input())
club_card = str(input())

discount = 0
final_price = 0

if club_card == "Yes":
    if type_fuel == "Gas":
        gas_price_liter = GAS - DISCOUNT_GAS
        gas_price_full = gas_price_liter * quantity_fuel
        if quantity_fuel > 25:
            discount += 0.1
        elif quantity_fuel >= 20:
            discount += 0.08
        final_price = gas_price_full - gas_price_full * discount
    elif type_fuel == "Gasoline":
        gasoline_price_liter = GASOLINE - DISCOUNT_GASOLINE
        gasoline_price_full = gasoline_price_liter * quantity_fuel
        if quantity_fuel > 25:
            discount += 0.1
        elif quantity_fuel >= 20:
            discount += 0.08
        final_price = gasoline_price_full - gasoline_price_full * discount
    elif type_fuel == "Diesel":
        diesel_price_liter = DIESEL - DISCOUNT_DIESEL
        diesel_price_full = diesel_price_liter * quantity_fuel
        if quantity_fuel > 25:
            discount += 0.1
        elif quantity_fuel >= 20:
            discount += 0.08
        final_price = diesel_price_full - diesel_price_full * discount
elif club_card == "No":
    if type_fuel == "Gas":
        gas_price_liter = GAS
        gas_price_full = gas_price_liter * quantity_fuel
        if quantity_fuel > 25:
            discount += 0.1
        elif quantity_fuel >= 20:
            discount += 0.08
        final_price = gas_price_full - gas_price_full * discount
    elif type_fuel == "Gasoline":
        gasoline_price_liter = GASOLINE
        gasoline_price_full = gasoline_price_liter * quantity_fuel
        if quantity_fuel > 25:
            discount += 0.1
        elif quantity_fuel >= 20:
            discount += 0.08
        final_price = gasoline_price_full - gasoline_price_full * discount
    elif type_fuel == "Diesel":
        diesel_price_liter = DIESEL
        diesel_price_full = diesel_price_liter * quantity_fuel
        if quantity_fuel > 25:
            discount += 0.1
        elif quantity_fuel >= 20:
            discount += 0.08
        final_price = diesel_price_full - diesel_price_full * discount

print(f"{final_price:.2f} lv.")
