#Don't change the code below
student_scores = input("Input a list of studen scores: ").split()
for i in range(0, len(student_scores)):
  student_scores[i] = int(student_scores[i])
print(student_scores)

#Write your code below this row

chair = 0
list = student_scores

for i in list:
    if i > chair:
        
        chair = i


print(chair)