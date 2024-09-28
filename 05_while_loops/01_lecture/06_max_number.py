import sys

user_input = input()

max_number = -sys.maxsize

while user_input != "Stop":
    number = int(user_input)
    if number > max_number:
        max_number = number
    user_input = input()

print(max_number)