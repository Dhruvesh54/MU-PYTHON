# 11	Python program to read the contents of a file in reverse order.

with open("example.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())