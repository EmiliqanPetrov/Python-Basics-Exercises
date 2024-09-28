day = str(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    result = "Working day"
elif day == "Saturday" or day == "Sunday":
    result = "Weekend"
else:
    result = "Error"

print(result)
