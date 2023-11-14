# Guess Beingsie's computer password
print('Beingsie\'s Computer')

# Ask user to guess password
guessed_password = int(input('Enter password: '))

# Password
password = 123456789

# While loop -
# If the guessed password is not correct
while guessed_password != password:
  guessed_password = int(input('Incorrect password. Please try again: '))

# If the password is guessed correctly
if guessed_password == password:
  print('Welcome Beingsie!')
