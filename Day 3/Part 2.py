import re

total_sum = 0
with open("text.txt", "r") as file:
    content = file.read()

matches = re.findall(r"mul\((\d+),\s*(\d+)\)", content)
for a, b in matches:
    total_sum += int(a) * int(b)

print(total_sum)
