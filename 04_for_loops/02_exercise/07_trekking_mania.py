count_groups = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

count_people = 0

for _ in range(count_groups):
    people = int(input())

    if people < 6:
        count_p1 += people
    elif people < 13:
        count_p2 += people
    elif people < 26:
        count_p3 += people
    elif people < 41:
        count_p4 += people
    else:
        count_p5 += people
        
    count_people += people


percent_p1 = (count_p1 / count_people) * 100
percent_p2 = (count_p2 / count_people) * 100
percent_p3 = (count_p3 / count_people) * 100
percent_p4 = (count_p4 / count_people) * 100
percent_p5 = (count_p5 / count_people) * 100

print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')
print(f'{percent_p4:.2f}%')
print(f'{percent_p5:.2f}%')