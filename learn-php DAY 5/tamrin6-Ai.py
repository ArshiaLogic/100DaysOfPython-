match_results = ["win", "loss", "draw", "win", "win", "draw"]

total_point = 0
for i in match_results:
  if i == "win":
    total_point += 3
  elif i == "draw":
    total_point += 1
print(total_point)      