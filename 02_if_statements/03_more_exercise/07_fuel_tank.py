NORM = 25

type_fuel = str(input())
tank_full = float(input())

if tank_full >= NORM and (type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas"):
    print(f"You have enough {type_fuel.lower()}.")
elif NORM > tank_full and (type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas"):
    print(f"Fill your tank with {type_fuel.lower()}!")
else:
    print("Invalid fuel!")
