# 90 Day Free Fares Program

# Import random module
import random

# Confirm if user has already enrolled before
membership_status = input("Have you enrolled before? (Y/N): ")

# Initialize membership status
active_membership = 0

if (
    membership_status == "y"
    or membership_status == "Y"
    or membership_status == "yes"
    or membership_status == "YES"
    or membership_status == "Yes"
    or membership_status == "yEs"
    or membership_status == "yeS"
):
    active_membership = True
    print(
        "Unfortunately you don't qualify for the 90 Day Free Fares as you're currently already an active customer. You can still qualify for the 20 free monthly fares."
    )
elif (
    membership_status == "n"
    or membership_status == "N"
    or membership_status == "no"
    or membership_status == "NO"
    or membership_status == "No"
    or membership_status == "nO"
):
    active_membership = False
    print("Great, you qualify for the 90 Day Free Fares Program!")
else:
    membership_status = input("Please enter (Y/N): ")

# Ask user for details
first_name = input("First Name: ")
middle_name = input("Middle Name: ")
last_name = input("Last Name: ")
street_address = input("Street Address: ")
city = input("City: ")
state = input("State: ")
zip_code = input("Zip Code: ")
phone_number = input("Phone Number: ")
email_address = input("Email Address: ")
birth_date = input("Birth Date: ")
gender = input("Gender: ")
ethnicity = input("Ethnicity: ")

# Create confirmation number
confirmation_number_id_identifier = "0000-"
confirmation_number = random.randint(100000, 999999)
confirmation_num = confirmation_number_id_identifier + str(confirmation_number)

# Print confirmation message
if active_membership == True:
	print("You have successfully enrolled into the 90 Day Free Fares Program!")
	print("Your confirmation number is", confirmation_num)
elif active_membership == False:
	print("You have successfully enrolled into the monthly 20 Free Fares Program!")
	print("Your confirmation number is", confirmation_num)
else:
	print("We're sorry, an error occured while processing your application.")
