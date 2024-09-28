floors = int(input())
rooms = int(input())

num_start = floors * 10

for floor in range(floors, 0, -1):
    for room in range(num_start, rooms + num_start):
        if floor == floors:
            print(f"L{room}", end=" ")
        elif floor % 2 == 1:
            print(f"A{room}", end=" ")
        elif floor % 2 == 0:
            print(f"O{room}", end=" ")
    print()
    num_start -= 10
