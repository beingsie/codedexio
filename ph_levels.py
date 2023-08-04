# Ask the user for a value between 0 and 14
ph = int(input('Pick a number between 0 and 14: '))

# Check whether a pH level is basic, acidic, or neutral
if ph > 7:
    print("pH level is: Basic")
elif ph < 7:
    print("pH level is: Acidic")
else:
    print("pH level is: Neutral")