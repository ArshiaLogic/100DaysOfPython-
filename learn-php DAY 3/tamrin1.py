#dont change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#your code below this line

bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"Your Bmi is {bmi}, you are underweight")
elif bmi < 25:
   print(f"Your Bmi is {bmi}, you are normal weight")
elif bmi < 30:
   print(f"Your Bmi is {bmi}, you are overweight")
elif bmi < 35:
   print(f"Your Bmi is {bmi}, you are obese")
else:
    print(f"Your Bmi is {bmi}, you are clinically obese.")