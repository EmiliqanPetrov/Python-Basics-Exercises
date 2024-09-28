name_actor = input()
points = float(input())
count_judges = int(input())

for _ in range(count_judges):
    judge_name = input()
    points_by_judge = float(input())

    points += (len(judge_name) * points_by_judge) / 2

    if points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
        exit()

print(f"Sorry, {name_actor} you need {1250.5 - points:.1f} more!")
