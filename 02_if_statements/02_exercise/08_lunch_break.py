def my_ceil(x):
    x_int = int(x)
    if type(x) == float and x != x_int:
        x = int(x)
        x += 1
    return x

LUNCH = 1 / 8
FREE_TIME = 1 / 4

series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length * LUNCH
free_time = break_length * FREE_TIME
leftover = break_length - lunch_time - free_time

if leftover >= episode_length:
    left_time = leftover - episode_length

    left_time = my_ceil(left_time)

    print(f"You have enough time to watch {series_name} and left with {left_time:.0f} minutes free time.")
elif leftover < episode_length:
    more_needed = episode_length - leftover

    if type(more_needed) == float:
        more_needed = int(more_needed)
        more_needed += 1

    print(f"You don't have enough time to watch {series_name}, you need {more_needed:.0f} more minutes.")