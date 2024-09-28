width = int(input())
length = int(input())
height = int(input())

free_space = width * height * length

command = input()

space_taken = 0

while command != "Done" and space_taken < free_space:
    curr_sqr_meters = int(command)
    space_taken += curr_sqr_meters
    if free_space <= space_taken:
        break

    command = input()

if command == "Done":
    print(f"{free_space - space_taken} Cubic meters left.")

if free_space <= space_taken:
    print(f"No more free space! You need {space_taken - free_space} Cubic meters more.")