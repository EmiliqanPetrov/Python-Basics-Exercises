DAYS_YEAR = 365
MINUTE_HOUR = 60
NORM = 30000
WORKDAY = 63
HOLIDAY = 127

holidays_count = int(input())

holidays_time = holidays_count * HOLIDAY

workdays_count = DAYS_YEAR - holidays_count
workdays_time = workdays_count * WORKDAY

full_time = holidays_time + workdays_time

if NORM >= full_time:
    leftover = NORM - full_time
    hours = leftover // MINUTE_HOUR
    minutes = leftover % MINUTE_HOUR
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    more_needed = full_time - NORM
    hours = more_needed // MINUTE_HOUR
    minutes = more_needed % MINUTE_HOUR
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
