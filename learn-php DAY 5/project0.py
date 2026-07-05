# #Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#------------------input------------------
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your Password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


#teacher code fuck fuck fuck

nr_letters = 3
nr_numbers = 4
nr_symbols = 2
password_list = []

for i in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for i in range (1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

for i in range (1, nr_symbols + 1):
  password_list.append(random.choice(symbols))


random.shuffle(password_list)
password = ""
for i in password_list:
  password += i

print(password)





# #my shit code
# #------------------letter randomizer------------------
# list_a = []
# for i in range(0, nr_letters):
#   n = (random.randint(0, len(letters) - 1))
#   list_a.append(letters[n])

# #------------------symbol randomizer------------------  
# list_b = []
# for i in range(0, nr_symbols):
#   n = (random.randint(0, len(symbols) - 1))
#   list_b.append(symbols[n])

# #------------------number randomizer------------------  
# list_c = []
# for i in range(0, nr_numbers):
#   n = (random.randint(0, len(numbers) - 1))
#   list_c.append(numbers[n])


# #------------------Random list------------------  
# random_list = list_a + list_b + list_c

# #------------------Random randomizer------------------  
# new_random_list = []
# for i in range(0, len(random_list)):
#   n = (random.randint(0, len(random_list) - 1))
#   new_random_list.append(random_list[n])

# #------------------OUTPUT------------------  
# print(("Here is your password: ") + ''.join(new_random_list))


  

