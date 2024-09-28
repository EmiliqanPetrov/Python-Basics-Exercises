age = float(input())
gender = str(input())

title = ""

if gender == "m":
    if age >= 16:
        title = "Mr."
    else:
        title = "Master"
elif gender == "f":
    if age >= 16:
        title = "Ms."
    else:
        title = "Miss"

print(title)