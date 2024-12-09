#doesnt work
with open("text2.txt", "r") as file:
    arr = [list(line.strip().split()) for line in file]

"""for i in range(len(arr)):
    flag = False
    for j in range(len(arr[i])-1):
        if (int(arr[i][j+1]) > int(arr[i][j]) and int(arr[i][j+1]) < int(arr[i][j])+2):
            print(*arr[i])
            print("increasing")
            print("")
        else:"""

def safe(ar):
    for i in range(1, len(ar)):
        diff = abs(int(ar[i]) - int(ar[i-1]))
        if diff < 1 or diff > 3:
            return False

    increasing = all(ar[i] < ar[i+1] for i in range(len(ar)-1))
    decreasing = all(ar[i] > ar[i+1] for i in range(len(ar)-1))

    return increasing or decreasing


count = 0
for i in range(len(arr)):
    print(*arr[i])
    if safe(arr[i]):
        count += 1

    print(count)
print(f"count: {count}")
