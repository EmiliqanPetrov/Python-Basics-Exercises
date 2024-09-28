deposit_amount = float(input())
deposit_time = int(input())
deposit_percent = float(input()) /100

total_amount = deposit_amount + deposit_time * ((deposit_amount * deposit_percent) / 12)

print(total_amount)