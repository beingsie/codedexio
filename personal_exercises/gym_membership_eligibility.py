'''
    Gym Membership Eligibility Checker
'''

# Ask user for age
user_age = int(input("What is your age: "))
# Ask the user about their fitness level
user_fitness_level = input("What is your fitness level? (high/medium/low): ").lower()
# Ask user for any medical conditions
user_medical_conditions = input("Do you have any medical conditions? (yes/no): ").lower()
has_medical_condition = user_medical_conditions == "yes"


'''
    Criteria to determine eligibility (Relational operators)
'''

# Age eligibility
is_old_enough = user_age >= 16

# Fitness level
fitness_level_high = user_fitness_level == "high"
fitness_level_medium = user_fitness_level == "medium"
fitness_level_low = user_fitness_level == "low"

'''
    Membership eligibility (Logical operators)
'''

# If user is 16 to 30 years old and has a "high" or "medium" fitness level
eligible_fitness_level = (is_old_enough and user_age <= 30) and (fitness_level_high or fitness_level_medium)
# If user is over 30 fitness level not considered
fitness_level_not_considered = user_age > 30

'''
    Display results
'''

print("Age: ", user_age)
print("Fitness level: ", user_fitness_level.capitalize())
print("Has medical conditions: ", user_medical_conditions.capitalize())
print("Is old enough: ", is_old_enough)
print("Is Eligible Fitness Level: ", eligible_fitness_level)
print("Is Exempt from Eligible Fitness Level: ", fitness_level_not_considered)
print("Has Medical Condition: ", has_medical_condition)

if (eligible_fitness_level or fitness_level_not_considered) and not has_medical_condition:
    print("Congratulations! You are eligible for a gym membership!")
else:
    print("I'm sorry, you are not eligible for a gym membership.")