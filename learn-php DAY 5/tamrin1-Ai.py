answers = [2, 1, 2, 3, 2, 2, 1, 3, 2, 1]



anxious_count = 0
for i in answers:
  if i == 2:
    anxious_count += 1
if anxious_count >= 6:
  print("anxious")
  print("omg")   
elif anxious_count >= 3:
  print("maybe anxious")
else:
  print("you are ok in anxious")