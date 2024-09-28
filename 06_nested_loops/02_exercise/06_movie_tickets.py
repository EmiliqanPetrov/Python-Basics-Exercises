movie = input()
seats = int(input())

command = input()

count_tickets = 0
curr_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while movie != "Finish":
    while command != "End":
        count_tickets += 1
        curr_tickets += 1

        if command == "student":
            student_tickets += 1
        elif command == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1

        if curr_tickets == seats:
            break

        command = input()
    print(f"{movie} - {curr_tickets / seats * 100:.2f}% full.")

    curr_tickets = 0

    movie = input()
    if movie == "Finish":
        break

    seats = int(input())

    command = input()

print(f"Total tickets: {count_tickets}")
print(f"{student_tickets / count_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / count_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / count_tickets * 100:.2f}% kids tickets.")
