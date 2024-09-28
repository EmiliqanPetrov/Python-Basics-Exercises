import math

shape = input()
area = 0

if shape == "square":
    side_a = float(input())
    area = side_a ** 2
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif shape == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
elif shape == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height) / 2

print(f"{area:.3f}")
