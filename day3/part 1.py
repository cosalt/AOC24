arr = []
with open("text.txt", "r") as file:
  arr = [line for line in file]


sum = 0
for x in arr:
    line = str(x).split("mul(")
    for j in range(len(line)):
        temp = line[j].split(")", 1)

        temp2 = temp[0].split(",", 0)
        temp3 = temp2[0].split(",")
        if len(temp3) > 2 or len(temp3) == 1:
            continue
        else:
          print(temp3)
          if temp3[0].isdigit() and temp3[1].isdigit():
            sum += (int(temp3[0]) * int(temp3[1]))


print(sum)
