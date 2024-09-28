def is_prime(num):
    if num == 1:
        return "not_prime"
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "not_prime"
        else:
            return "prime"

command = input()

prime_sum = 0
not_prime_sum = 0

while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
    elif is_prime(number) == "not_prime":
        not_prime_sum += number
    elif is_prime(number) == "prime":
        prime_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")
