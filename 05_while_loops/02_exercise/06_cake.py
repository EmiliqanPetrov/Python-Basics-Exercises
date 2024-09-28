width = int(input())
length = int(input())

count_pieces = width * length

command = input()

total_pieces_taken = 0

while command != "STOP" and total_pieces_taken < count_pieces:
    curr_pieces = int(command)
    total_pieces_taken += curr_pieces
    if total_pieces_taken >= count_pieces:
        break

    command = input()


if command == "STOP":
    print(f"{count_pieces - total_pieces_taken} pieces are left." )

if total_pieces_taken >= count_pieces:
    print(f"No more cake left! You need {total_pieces_taken - count_pieces} pieces more.")