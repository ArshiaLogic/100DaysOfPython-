server_pings = [120, 85, 45, 92, 310, 55]

lowset_ping = 99999
for i in server_pings:
  if i < lowset_ping :
    lowset_ping = i
print(lowset_ping)
