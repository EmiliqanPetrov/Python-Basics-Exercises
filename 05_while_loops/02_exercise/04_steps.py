GOAL_STEPS = 10_000
END_COMMAND = "Going home"

command = input()

total_steps = 0

while command != END_COMMAND and total_steps < GOAL_STEPS:
    curr_steps = int(command)
    total_steps += curr_steps
    if total_steps >= GOAL_STEPS:
        break

    command = input()

if command == END_COMMAND:
    addition_steps = int(input())
    total_steps += addition_steps
    if total_steps >= GOAL_STEPS:
        print(f"Goal reached! Good job!\n{total_steps - GOAL_STEPS} steps over the goal!")
    else:
        print(f"{GOAL_STEPS - total_steps} more steps to reach goal.")

elif total_steps >= GOAL_STEPS:
    print(f"Goal reached! Good job!\n{total_steps - GOAL_STEPS} steps over the goal!")