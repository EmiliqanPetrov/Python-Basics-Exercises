NUMBER_PERCENT = 100

volume = int(input())
pipe1_hour = int(input())
pipe2_hour = int(input())
hours = float(input())

pipe1_liters = pipe1_hour * hours
pipe2_liters = pipe2_hour * hours
all_liters = pipe1_liters + pipe2_liters

if volume >= all_liters:
    percent_full = (all_liters / volume) * NUMBER_PERCENT
    pipe1_percent = (pipe1_liters / all_liters) * NUMBER_PERCENT
    pipe2_percent = (pipe2_liters / all_liters) * NUMBER_PERCENT
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%.")
else:
    overflow = all_liters - volume
    print(f"For {hours:.2f} hours the pool overflows with {overflow:.2f} liters.")