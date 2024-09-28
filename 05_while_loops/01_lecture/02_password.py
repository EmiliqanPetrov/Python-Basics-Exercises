name = input()
password = input()

attempt = input()

while attempt != password:
    attempt = input()

print(f"Welcome {name}!")