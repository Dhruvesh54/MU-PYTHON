# 3 Write a program that uses for loop to print all the odd, even numbers in the range input   by user.
x = int(input("Enter the range for number:"))
print("Odd numbers between 0 and ", x)
for i in range(0, x):
    if i % 2 != 0:
        print(i)
print("Even numbers between 0 and ", x)
for i in range(0, x):
    if i % 2 == 0:
        print(i)
