n = int(input())

command = input()

sum_grades = 0
sum_grades_final = 0
count = 0

while command != "Finish":
    count += 1
    for i in range(n):
        grade = float(input())
        sum_grades += grade
        sum_grades_final += grade
    print(f"{command} - {sum_grades / n:.2f}.")
    sum_grades = 0

    command = input()

print(f"Student's final assessment is {sum_grades_final / (count * n):.2f}.")