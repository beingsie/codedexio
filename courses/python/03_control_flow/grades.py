# Ask user for their grade
grade = int(input("What grade did you get on your test? "))

# Check if user grade is higher or lower than 55
if grade >= 55:
    # Print passed
    print("You've passed your test!")
else:
    # Print failed
    print("You've failed your test.")