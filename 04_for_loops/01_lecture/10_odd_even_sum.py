n = int(input())

odd_sum = 0
even_sum = 0

for _ in range(1, n + 1):
    curr_number = int(input())

    if _ % 2 == 0:
        odd_sum += curr_number
    else:
        even_sum += curr_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {abs(odd_sum - even_sum)}")