gpu_temps = [65, 72, 81, 89, 75, 92, 70]


danger = False
gpu_tempss = 0
for i in gpu_temps:
  if i > 85:
    danger = True
  
print(danger)
