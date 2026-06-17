age = input("What is your current age?")


#Write your code below this line
remain =  90 - int(age)

days = remain * 365

weeks = remain * 52

months = remain * 12

result = (f"You have {days} days, {weeks} weeks, and {months} months left.")

print(result)