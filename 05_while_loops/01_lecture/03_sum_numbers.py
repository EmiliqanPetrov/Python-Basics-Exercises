sum_numbers = int(input())
curr_number = int(input())

total_sum = curr_number

while total_sum < sum_numbers:
    curr_number = int(input())
    total_sum += curr_number

print(total_sum)
