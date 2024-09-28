hour = int(input())
weekday = input()

if weekday != "Sunday" and 10 <= hour <= 18:
    print("open")
else:
    print("closed")