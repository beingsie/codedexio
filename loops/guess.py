# Initialize 'guess' and 'tries' to use as variables inside the while loop
guess = 0
tries = 0

# While loop with a max of 5 tries
while guess != 6 and tries < 5:
  # Ask user to guess the number
  guess = int(input('Guess the number:  '))
  # Add 1 to tries if user guessed incorrectly (fails to exit loop)
  tries += 1

# Display messages when condition becomes false
if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')