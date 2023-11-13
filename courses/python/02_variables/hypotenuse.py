# Pythagorean Theorem

# Ask user for two numbers
user_num_1 = int(input('Enter a number: '))
user_num_2 = int(input('Enter a second number: '))

# Length of a short side
a = user_num_1 ** 2

# Length of another short side
b = user_num_2 ** 2

# Length of the hypotenuse
c = (a + b) ** 0.5

# Print the hypotenuse
print(c)