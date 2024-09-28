start = int(input())
end = int(input())

for num in range(start, end + 1):
    str_num = str(num)
    if int(str_num[0]) + int(str_num[2]) + int(str_num[4]) == int(str_num[1]) + int(str_num[3]) + int(str_num[5]):
        print(num, end=' ')
