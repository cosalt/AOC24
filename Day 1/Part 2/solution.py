same = 0
for i in left:
  temp = 0
  for j in right:
    if i == j:
      temp += 1
  same += (int(i) * temp)

print(same)
