width = float(input()) * 100
height = float(input()) * 100 - 100

width_places = width // 120
height_places = height // 70

all_places = width_places * height_places - 3

print(f"{all_places:.0f}")