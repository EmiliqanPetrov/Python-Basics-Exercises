HOUR_MINUTE = 60

hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())
result = ""

minutes_exam_time = hour_exam * HOUR_MINUTE + minute_exam
minutes_arrive_time = hour_arrive * HOUR_MINUTE + minute_arrive

if minutes_arrive_time > minutes_exam_time:
    result = "Late"
elif 0 <= abs(minutes_exam_time - minutes_arrive_time) <= 30:
    result = "On time"
else:
    result = "Early"

print(result)

if (minutes_arrive_time > minutes_exam_time) and ((minutes_arrive_time - minutes_exam_time) < 60):
    print(f"{abs(minutes_arrive_time - minutes_exam_time)} minutes after the start")
elif (minutes_arrive_time > minutes_exam_time) and ((minutes_arrive_time - minutes_exam_time) >= 60):
    hours = (minutes_arrive_time - minutes_exam_time) // HOUR_MINUTE
    minutes = (minutes_arrive_time - minutes_exam_time) % HOUR_MINUTE
    if minutes >= 10:
        print(f"{abs(hours)}:{abs(minutes)} hours after the start")
    else:
        print(f"{hours}:0{minutes} hours after the start")
elif (minutes_exam_time > minutes_arrive_time) and ((minutes_exam_time - minutes_arrive_time) >= 60):
    hours = (minutes_exam_time - minutes_arrive_time) // HOUR_MINUTE
    minutes = (minutes_exam_time - minutes_arrive_time) % HOUR_MINUTE
    if minutes >= 10:
        print(f"{abs(hours)}:{abs(minutes)} hours before the start")
    else:
        print(f"{abs(hours)}:0{abs(minutes)} hours before the start")
elif (minutes_exam_time > minutes_arrive_time) and ((minutes_exam_time - minutes_arrive_time) < 60):
    print(f"{abs(minutes_arrive_time - minutes_exam_time)} minutes before the start")

