import sys

user_input = input()

min_number = sys.maxsize

while user_input != "Stop":
    number = int(user_input)
    if number < min_number:
        min_number = number
    user_input = input()

print(min_number)