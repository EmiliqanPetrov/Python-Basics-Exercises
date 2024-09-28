n = int(input())

max_number = float("-inf")
total_sum = 0

for num in range(n):
    number = int(input())

    if number > max_number:
        max_number = number

    total_sum += number

total_sum -= max_number

if total_sum == max_number:
    print(f"Yes\nSum = {total_sum}")
else:
    print(f"No\nDiff = {abs(total_sum - max_number)}")
