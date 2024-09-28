FACEBOOK = 150.00
INSTAGRAM = 100.00
REDDIT = 50.00

tabs = int(input())
salary = int(input())

for _ in range(tabs):
    website = input()

    if website == "Facebook":
        salary -= FACEBOOK
    elif website == "Instagram":
        salary -= INSTAGRAM
    elif website == "Reddit":
        salary -= REDDIT

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(f"{salary:.0f}")