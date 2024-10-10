# 10	Write a program to demonstrate the File handling functionality in python.

with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("It demonstrates file handling in Python.\n")

with open("example.txt", "r") as file:
    content = file.read()


with open("example.txt", "a") as file:
    file.write("This line was appended to the file.\n")


with open("example.txt", "r") as file:
    updated_content = file.read()
