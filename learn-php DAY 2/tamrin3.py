print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? ")) # تغییر به int

# منطق مرحله‌به‌مرحله با نام‌گذاری‌های استانداردتر
tip_percentage = (percent / 100)
tip_amount = (bill * tip_percentage)
total_amount = (bill + tip_amount)
bill_per_person = (total_amount / people)

# گرد کردن تا دو رقم اعشار برای نمایش پول
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")


#lear 
# test = 10 / 5
# test = "{:.2f}".format(test)
# print(test)