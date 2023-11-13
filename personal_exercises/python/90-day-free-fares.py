# 90 Day Free Fares Program

# Import random module
import random

# Confirm if user has already enrolled before
enrolled = input("Have you enrolled before? (Y/N): ")

if (
    enrolled == "y"
    or enrolled == "Y"
    or enrolled == "yes"
    or enrolled == "YES"
    or enrolled == "Yes"
    or enrolled == "yEs"
    or enrolled == "yeS"
):
    is_enrolled = True
    print(
        "Unfortunately you don't qualify for the 90 Day Free Fares as you're currently already an active customer. You can still qualify for the 20 free monthly fares."
    )
elif (
    enrolled == "n"
    or enrolled == "N"
    or enrolled == "no"
    or enrolled == "NO"
    or enrolled == "No"
    or enrolled == "nO"
):
    is_enrolled = False
    print("Great, you qualify for the 90 Day Free Fares Program!")
else:
    enrolled = input("Please enter (Y/N): ")

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
is_enrolled = 0

# Create confirmation number
confirmation_number_id_identifier = "0000-"
confirmation_number = random.randint(100000, 999999)
confirmation_num = confirmation_number_id_identifier + str(confirmation_number)

# Print confirmation message
print(
    "You have successfully enrolled into the 90 Day Free Fares Program! Your confirmation number is "
    + confirmation_num
)
