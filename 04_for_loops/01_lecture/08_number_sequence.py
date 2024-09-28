n = int(input())

numbers_list = []

for _ in range(1, n + 1):
    curr_number = int(input())

    numbers_list.append(curr_number)

print(f"Max number: {max(numbers_list)}")
print(f"Min number: {min(numbers_list)}")