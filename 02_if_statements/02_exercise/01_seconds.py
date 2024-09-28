first = int(input())
second = int(input())
third = int(input())

sum_seconds = first + second + third
minutes = sum_seconds // 60
left_seconds = sum_seconds % 60

if left_seconds < 10:
    print(f"{minutes}:0{left_seconds}")
elif left_seconds >= 10:
    print(f"{minutes}:{left_seconds}")