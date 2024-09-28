pages_count = int(input())
pages_hour = int(input())
day_count = int(input())

time_sum = pages_count // pages_hour
hours_day = time_sum // day_count

print(hours_day)