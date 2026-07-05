login_attempts = ["success", "fail", "fail", "success", "fail", "fail", "fail", "success"]

lock = False
total_lcok = 0
for i in login_attempts:
  if i == "fail":
    total_lcok +=1
    if total_lcok >= 4:
      lock = True
    
print(lock)  