#Practice Code
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#____________ True Love Calculator ____________
combined_names = name1.lower() + name2.lower()

#____________ True Calculator ____________
count_True = combined_names.count("t")
count_True += combined_names.count("r")
count_True += combined_names.count("u")
count_True += (combined_names.count("e"))

#____________ Love Calculator ____________
count_love = combined_names.count("l")
count_love += combined_names.count("o")
count_love += combined_names.count("v")
count_love += (combined_names.count("e"))

#____________Calculator____________
True_love_percent = (count_True * 10) + count_love

#____________ Love interpretation ____________
if True_love_percent < 10 or True_love_percent > 90:
 print(f"Your score is {True_love_percent}, you go together like coke and mentos.")
elif True_love_percent > 40 and True_love_percent < 50:
 print(f"Your score is {True_love_percent}, you are alright together.")
else:
  print(f"Your score is {True_love_percent}")

#this is my code bich yaaa