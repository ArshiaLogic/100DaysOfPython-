# Don't change the code below
print("Welcome to the Grand Chess Tournament!")
level = input("What is your level? N, C, or M? ")
custom_board = input("Do you want a customized chess board? Y or N ")
tshirt = input("Do you want a tournament T-shirt? Y or N ")

# Write your code below this line
bill = 0

if level == "N":
  bill = 20
if level == "C":  
  bill = 30
if level == "M":
  bill = 50
if custom_board == "Y":
 if level == "N":
   bill += 5 
 elif level == "C": 
  bill += 10
 elif level == "M": 
  bill += 15
if tshirt == "Y":
  bill += 7
print (f"You must pay ${bill}")