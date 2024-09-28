n = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for _ in range(n):
    number = int(input())

    if number < 200:
        count_p1 += 1
    elif number < 400:
        count_p2 += 1
    elif number < 600:
        count_p3 += 1
    elif number < 800:
        count_p4 += 1
    else:
        count_p5 += 1

total_numbers = count_p1 + count_p2 + count_p3 + count_p4 + count_p5

percent_p1 = (count_p1 / total_numbers) * 100
percent_p2 = (count_p2 / total_numbers) * 100
percent_p3 = (count_p3 / total_numbers) * 100
percent_p4 = (count_p4 / total_numbers) * 100
percent_p5 = (count_p5 / total_numbers) * 100

print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')
print(f'{percent_p4:.2f}%')
print(f'{percent_p5:.2f}%')

