# User input
number = int(input("Enter a number: "))

# Initialize sum
sum = 0

# Get all numbers leading up to user number
for x in range(1, number +1):
    # Square all numbers from range
    square = x ** 2
    # Calculate the sum of the squares of numbers
    sum = sum + square

# Print sum of numbers
print(sum)