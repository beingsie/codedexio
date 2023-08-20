# Ask user for current number of the month
current_month = int(input("What is the current month number: "))

# Display month
if current_month == 1 or current_month == 2 or current_month == 3:
    print("Winter 🥶")
elif current_month == 4 or current_month == 5 or current_month == 6:
    print("Spring 🌱")
elif current_month == 7 or current_month == 8 or current_month == 9:
    print("Summer 🌻")
elif current_month == 10 or current_month == 11 or current_month == 12:
    print("Autumn 🍂")
else:
    print("Invalid")