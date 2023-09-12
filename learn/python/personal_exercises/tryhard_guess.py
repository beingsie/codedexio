# Exercise: Number Guessing Game with Limited Tries and Hints

# Initialize 'guess' and 'tries' to use as variables inside the while loop
guess = 0
tries = 0

# Loop
while guess != 69 and tries < 7:
    # Ask user to guess a number between 1 and 100
    guess = int(input("Guess a secret number between 1 and 100: "))

    # Add 1 to a max of 7 tries
    tries += 1

    # Hints
    guess_too_low = guess <= 64
    guess_too_high = guess >= 74
    guess_close = (guess >= 65) or (guess <= 73)

    # Give user a hint if guess was too low
    if guess_too_low:
        print("Too low! Guess again!")
    # Give user a hint if guess was too high
    elif guess_too_high:
        print("Too high! Guess again!")
    # Give user a hint if guess was close
    elif guess_close:
        print("OMG very close! Guess again!")

# Message user when out of tries
if guess != 69:
    print("Whoops, you're all out of tries! Thanks for playing!")
# Message user if guessed correctly
else:
    print("Correct! You're a wizard!")