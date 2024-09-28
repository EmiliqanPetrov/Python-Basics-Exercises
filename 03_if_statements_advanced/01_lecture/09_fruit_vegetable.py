fruit = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable = ["tomato", "cucumber", "pepper", "carrot"]

food = input()

if (food == fruit[0]
        or food == fruit[1]
        or food == fruit[2]
        or food == fruit[3]
        or food == fruit[4]
        or food == fruit[5]):
    print("fruit")
elif food == vegetable[0] or food == vegetable[1] or food == vegetable[2] or food == vegetable[3]:
    print("vegetable")
else:
    print("unknown")
