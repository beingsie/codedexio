# Import random module
import random

# Ask user for a question
question = input('Ask a question: ')

# Generate random number
random_num = random.randint(1, 9)

# Logic
if random_num == 1:
  print('Magic 8 Ball: Yes - definitely.')
elif random_num == 2:
  print('Magic 8 Ball: It is decidedly so.')
elif random_num == 3:
  print('Magic 8 Ball: Without a doubt.')
elif random_num == 4:
  print('Magic 8 Ball: Reply hazy, try again.')
elif random_num == 5:
  print('Magic 8 Ball: Ask again later.')
elif random_num == 6:
  print('Magic 8 Ball: Better not tell you now.')
elif random_num == 7:
  print('Magic 8 Ball: My sources say no.')
elif random_num == 8:
  print('Magic 8 Ball: Outlook not so good.')
else:
  print('Magic 8 Ball: Very doubtful.')
