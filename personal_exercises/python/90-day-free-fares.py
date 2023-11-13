# 90 Day Free Fares Program

# Import random module
import random

# Initialize membership status
active_membership = 0

# Confirm if user has already enrollment_status before
enrollment_status = input("Have you enrollment_status before? (Y/N): ")

if (
    enrollment_status == "y"
    or enrollment_status == "Y"
    or enrollment_status == "yes"
    or enrollment_status == "YES"
    or enrollment_status == "Yes"
    or enrollment_status == "yEs"
    or enrollment_status == "yeS"
):
    active_membership = True
    print(
        "Unfortunately you don't qualify for the 90 Day Free Fares as you're currently already an active customer. You can still qualify for the 20 free monthly fares."
    )
elif (
    enrollment_status == "n"
    or enrollment_status == "N"
    or enrollment_status == "no"
    or enrollment_status == "NO"
    or enrollment_status == "No"
    or enrollment_status == "nO"
):
   active_membership = False
    print("Great, you qualify for the 90 Day Free Fares Program!")
else:
    enrollment_status = input("Please enter (Y/N): ")

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
	print('You have successfully enrolled into the 90 Day Free Fares Program!')
	print('Your confirmation number is', confirmation_num)
elif active_membership == False:
	print('You have successfully enrolled into the monthly 20 Free Fares Program!')
	print('Your confirmation number is', confirmation_num)
else:
	print('We're sorry, an error occured while processing your application.')
