mammal = ["dog"]
reptile = ["crocodile", "tortoise", "snake"]

animal = str(input())

if animal == mammal[0]:
    result = "mammal"
elif animal == reptile[0] or animal == reptile[1] or animal == reptile[2]:
    result = "reptile"
else:
    result = "unknown"

print(result)
