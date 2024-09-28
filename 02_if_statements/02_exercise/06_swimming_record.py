record = float(input())
length_meters = float(input())
meter_per_second = float(input())

time_swimming = length_meters * meter_per_second
time_additional = (length_meters // 15) * 12.5
full_time = time_swimming + time_additional

if record > full_time:
    new_record = full_time
    print(f" Yes, he succeeded! The new world record is {new_record:.2f} seconds.")
else:
    slower = full_time - record
    print(f"No, he failed! He was {slower:.2f} seconds slower.")