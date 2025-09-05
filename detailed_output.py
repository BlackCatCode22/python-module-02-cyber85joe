# Define function with logic to find the largest integer
def largestOfThree(num1, num2, num3):
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
    return largest

# Define function to create a detailed output message
def detailedMessage(num1, num2, num3, largest):
    if largest == num1:
        largest_var = "num1"
    elif largest == num2:
        largest_var = "num2"
    else:
        largest_var = "num3"
   
    message = (f"Message to User: You entered three numbers, {num1}, {num2}, and {num3}. "
               f"The first whole number you entered was assigned to a variable named num1, "
               f"the second ({num2}) to num2, and finally the third ({num3}) was assigned to num3. "
               f"Your input was processed and the largest number you entered was {largest}, "
               f"which belonged to an integer variable named {largest_var}.")
    print(message)

# User input
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Function call
largest = largestOfThree(num1, num2, num3)

# Call the detailed message function
detailedMessage(num1, num2, num3, largest)

quit()