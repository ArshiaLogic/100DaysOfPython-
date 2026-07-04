row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasue? ")

#__________________ Number divider __________________
position = int(position)

num1 = position // 10
num2 = position % 10
#__________________ Inputer __________________

map[num2 - 1][num1 - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

