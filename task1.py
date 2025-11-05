# Program: Basic Mathematical Operations

# Step 1: Take two numbers as input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 2: Perform basic mathematical operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Step 3: Display the results
print("\nResults:")
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
# Program: Personalized Greeting

# Step 1: Take user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Concatenate first name and last name into full name
full_name = first_name + " " + last_name

# Step 3: Print a personalized greeting message
print("Hello,", full_name + "! Welcome to Python programming.")
