count_fails_possible = int(input())

count_fails = 0
sum_grades = 0
count_problems = 0
last_problem = ""

problem_name = input()
grade = float(input())

while count_fails_possible > count_fails and problem_name != "Enough":
    last_problem = problem_name
    sum_grades += grade
    count_problems += 1

    if grade <= 4:
        count_fails += 1
        if count_fails == count_fails_possible:
            break
        problem_name = input()
        if problem_name == "Enough":
            break
        grade = float(input())
        continue

    problem_name = input()
    if problem_name == "Enough":
        break
    grade = float(input())

if count_fails == count_fails_possible:
    print(f"You need a break, {count_fails_possible} poor grades.")
elif problem_name == "Enough":
    print(f"Average score: {sum_grades / count_problems:.2f}")
    print(f"Number of problems: {count_problems}")
    print(f"Last problem: {last_problem}")