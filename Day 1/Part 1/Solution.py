left, right = [], []
with open("text.txt", "r") as file:
  left, right = map(list, zip(*(line.split() for line in file)))

left.sort()
right.sort()
sum = 0
# i is n, j is value
for i, j in enumerate(left):
  sum += abs((int(left[i]) - int(right[i])))


print(sum)
