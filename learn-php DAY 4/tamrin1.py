import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

# names_random = random.choice(names)
total = len(names)
number = random.randint(0, total - 1)

print(f"{names[number]} is going to buy the meal today!")