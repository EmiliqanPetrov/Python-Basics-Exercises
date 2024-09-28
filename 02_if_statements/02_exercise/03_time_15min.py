hours_read = int(input())
minutes_read = int(input())

all_minutes = hours_read * 60 + minutes_read + 15
hours = all_minutes // 60
minutes = all_minutes % 60

if hours == 24:
    type_hours = 0
else:
    type_hours = hours

if minutes < 10:
    print(f"{type_hours}:0{minutes}")
else:
    print(f"{type_hours}:{minutes}")