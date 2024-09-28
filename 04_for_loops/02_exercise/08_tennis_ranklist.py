import math

count_tournaments = int(input())
points = int(input())
start_points = points

wins = 0

for _ in range(count_tournaments):
    tournament_stage = input()

    if tournament_stage == "W":
        points += 2000
        wins += 1
    elif tournament_stage == "F":
        points += 1200
    elif tournament_stage == "SF":
        points += 720

points_won = points - start_points

print(f"Final points: {points}")
print(f"Average points: {math.floor(points_won / count_tournaments)}")
print(f"{wins / count_tournaments * 100:.2f}%")