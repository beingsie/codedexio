# Import random module
import random

# Randomize value from 1-6 and assign to dice
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

# Calculate the sum of the dice
total = dice_1 + dice_2

# Initialize user guess
guess = int(input("You just rolled 2 dice. Guess the total value of the dice: "))

# Ask user to guess dice total
while guess != total:
    guess = int(input("Oof, try again: "))

# Print message if correct
if guess == total:
    print("You got it!")