CM_TO_L = 1000

length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume_full = (length * width * height) / CM_TO_L
volume_solids = 17 / 100
liters_water = volume_full * (1 - volume_solids)

print(liters_water)


