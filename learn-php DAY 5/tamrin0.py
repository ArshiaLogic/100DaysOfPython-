#Don't change the code below
student_heights = input("Input a list of student heights ").split()
for i in range(0, len(student_heights)):
  student_heights[i] = int(student_heights[i])
print(student_heights)


#Write your code below this row
#No len() & No sum()

total_ppl = 0
total_heights = 0
for height in student_heights:
  total_heights += height
  total_ppl += 1
avarage_heights = round(total_heights / total_ppl)
print(avarage_heights)