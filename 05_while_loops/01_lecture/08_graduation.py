name = input()

grade = float(input())

sum_grades = 0
student_class = 1
count_fails = 0

while student_class <= 12:
    if grade < 4:
        count_fails += 1
        if count_fails > 1:
            print(f"{name} has been excluded at {student_class} grade")
            break
        grade = float(input())
        continue

    sum_grades += grade

    if student_class == 12:
        break

    grade = float(input())
    student_class += 1

if student_class == 12 and count_fails < 2:
    avg_grade = sum_grades / 12
    print(f"{name} graduated. Average grade: {avg_grade:.2f}")