# Display each planet's relative gravity
print('''
The year is 2199...
We have become an interplanetary species and can travel to other planets in the solar system! 🚀

Here are planets and their relative gravities:
      
1 - Mercury: 0.38
2 - Venus: 0.91
3 - Mars: 0.38
4 - Jupiter: 2.53
5 - Saturn: 1.07
6 - Uranus: 0.89
7 - Neptune: 1.14

''')
      
# Ask the user for a number that correlates with a planet
user_choice = int(input("Pick a number from the list to find out what your weight would be on that planet: "))
      
# Ask the user what their Earth weight is
user_weight = int(input("What is your earth weight: "))

# Display user weight
print(f"Earth weight: {user_weight}lb.")

# Assign planet weights
weight_mercury = 0.38
weight_venus = 0.91
weight_mars = 0.38
weight_jupiter = 2.53
weight_saturn = 1.07
weight_uranus = 0.89
weight_neptune= 1.14

# Initialize relative weight and chosen planet
relative_weight = 0
chosen_planet = 0

# Assign planets to their number on the list
if user_choice == 1:
    relative_weight = weight_mercury
    chosen_planet = "Mercury"
elif user_choice == 2:
    relative_weight = weight_venus
    chosen_planet = "Venus"
elif user_choice == 3:
    relative_weight = weight_mars
    chosen_planet = "Mars"
elif user_choice == 4:
    relative_weight = weight_jupiter
    chosen_planet = "Jupiter"
elif user_choice == 5:
    relative_weight = weight_saturn
    chosen_planet = "Saturn"
elif user_choice == 6:
    relative_weight = weight_uranus
    chosen_planet = "Uranus"
elif user_choice == 7:
    relative_weight = weight_neptune
    chosen_planet = "Neptune"
else:
    print("Error: Your input was not a choice from the list.")

# Calculate user's new weight on chosen planet and assign to destination weight
destination_weight = user_weight * relative_weight

# Display destination weight
print(f"Your weight on {chosen_planet} would be {destination_weight}lb.")