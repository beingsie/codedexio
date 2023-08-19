# Exercise: Car Rental Eligibility

'''
    Take user input
'''
# Ask user for age
user_age = int(input("What is your age? "))
# Ask user for license
has_valid_license = input("Do you have a valid drivers license? ").lower() == "yes"
# Ask user for insurance
has_insurance = input("Do you have car insurance? ").lower() == "yes"

'''
    Relational operators
'''
is_old_enough = user_age >= 21
is_young_enough = user_age <= 75

'''
    Logical operators
'''
can_drive = (is_old_enough and is_young_enough) and (has_valid_license and has_insurance)
cannot_drive = not can_drive

'''
    Display results
'''
print("Driver age: ", user_age)
print("Has valid drivers license: ", has_valid_license)
print("Has insurance: ", has_insurance)
print("Is old enough: ", is_old_enough)
print("Is young enough: ", is_young_enough)
print("Can drive: ", can_drive)
print("Cannot drive: ", cannot_drive)

if can_drive:
    print("Congratulations, you are eligable to drive!")
else:
    print("I'm sorry, you are not eligable to drive.")