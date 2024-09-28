start = int(input())
end = int(input())
number = int(input())

comb_counter = 0

flag = False

for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        comb_counter += 1
        if x1 + x2 == number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f"Combination N:{comb_counter} ({x1} + {x2} = {number})")
else:
    print(f"{comb_counter} combinations - neither equals {number}")