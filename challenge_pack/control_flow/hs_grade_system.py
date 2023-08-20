# Ask user for their current high school grade level
grade = int(input("What high school grade level are you in: "))

# Display users high school grade level
if grade == 9:
    print("Freshman")
elif grade == 10:
    print("Sophomore")
elif grade == 11:
    print("Junior")
elif grade == 12:
    print("Senior")
else:
    print("TBD")