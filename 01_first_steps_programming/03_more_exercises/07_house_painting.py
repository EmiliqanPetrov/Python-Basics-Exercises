x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 ** 2
side_walls_no_window = 2 * side_wall - 2 * window
back_wall = x ** 2
door = 2.4
front_back_walls = 2 * back_wall - 2.4
full_walls = side_walls_no_window + front_back_walls
green_paint = full_walls / 3.4

rectangels_roof = 2 * (x * y)
triangels_roof = 2 * (x * h / 2)
full_roof = rectangels_roof + triangels_roof
red_paint = full_roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
