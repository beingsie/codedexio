# Import random module
import random

# Create list of random answers
answer_list = [
    # Random answers
    "Yes - definitely.",
    "It is decidedly so.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# Ask user to pick a question
user_question = str(input("What is your question? "))

# Print random generated answer
print(random.choice(answer_list))