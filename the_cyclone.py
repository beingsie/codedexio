# Assign required height & credit
height_requirement = int(40)
credits_requirement = int(10)

# Ask user for height & current available credit
user_height = int(input("How tall are you in inches? "))
user_credits = int(input("How many credits do you have? "))

# Check if user meets both requirements
if user_height >= height_requirement and user_credits >= credits_requirement:
    print("Enjoy the ride 🎢")
# Check if user passes credits requirement but fails height requirement
elif user_credits >= credits_requirement and user_height < height_requirement:
    print("You are not tall enough to ride 🫠")
# Check if user passes height requirement but fails credits requirement
elif user_height >= height_requirement and user_credits < credits_requirement:
    print("You don't have enough credits 😭")
# Otherwise user fails all requirements
else:
    print("You do not meet the requirements to ride 🙈")