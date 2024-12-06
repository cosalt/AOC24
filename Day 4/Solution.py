#doesnt work
with open("text.txt", "r") as file:
  arr = [list(line.strip()) for line in file]

for line in arr:
  print("".join(line))



#horizontal back and forwards
onedarray = [x for i in arr for x in i]
print(onedarray)
onedarray = ''.join(onedarray)
print(onedarray)
print(f"horizontal count = {onedarray.count('XMAS')}")
onedarray = onedarray[::-1]
print(f"backwards count = {onedarray.count('XMAS')}")

#vertical
verticalarr = [[row[i] for row in arr] for i in range(len(arr[0]))]
print(verticalarr)
sum = 0
for j in verticalarr:
    temp = ''.join(j)
    x = temp.count("XMAS")
    sum += x
    temp = temp[::-1]
    x = temp.count("XMAS")
    sum += x
print(f"vertical: {sum}")


def diagonally(arr):
    n = len(arr)
    count =0
    for i in range(n):
        for j in range(n):
            #print(f"Diagonals from element ({i},{j})")

            diag1 = []
            row, col = i, j
            while row < n and col < n:
                diag1.append(arr[row][col])
                row += 1
                col += 1
            #print(diag1)
            temp = ''.join(diag1)
            count += temp.count("XMAS")
            temp = temp[::-1]
            count += temp.count("XMAS")

            diag2 = []
            row, col = i, j
            while row < n and col >= 0:
                diag2.append(arr[row][col])
                row = row + 1
                col = col - 1
            #print(diag2)
            temp = ''.join(diag2)
            count += temp.count("XMAS")
            temp = temp[::-1]
            count += temp.count("XMAS")
    return count
print(f"diagonally: {diagonally(arr)}")
