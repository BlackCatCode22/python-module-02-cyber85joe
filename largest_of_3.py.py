# largest_of_3.py
# Program to find the largest of three integers using nested if statements

# Get three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Nested if logic to find the largest
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

# Output the result
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")