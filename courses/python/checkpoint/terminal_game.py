# Import Random Module
import random

# Characters
possessed_bear = "possessed bear"  # Temp name
punching_baby = "punching baby"  # Temp name

# Universal Stats
xp = 0

# - Character Stats
# Possessed Bear
possessed_bear_hp = 250
possessed_bear_atk = 3

# Punching Baby
punching_baby_hp = 90
punching_baby_atk = 15

# Player name
player_name = input("Enter your player name: ")
print("")

# Welcome message
print(f"Welcome to Monster Royale {player_name.capitalize()}!")

# - Character Selection
# Display list of characters
print(f"[Characters]")
print(f"> 1. {punching_baby.title()}")
print(f"- HP: {punching_baby_hp}")
print(f"- Attack Power: {punching_baby_atk}")
print(f"> 2. {possessed_bear.title()}")
print(f"- HP: {possessed_bear_hp}")
print(f"- Attack Power: {possessed_bear_atk}")

# Character Selection
selected_character = input("Choose a character: ").lower()

# Loop user to select an available character if no available character is selected
while (selected_character != punching_baby and selected_character != "1") and (selected_character != possessed_bear and selected_character != "2"):
     selected_character = input("Please select an available character: ").lower()

if selected_character == punching_baby.lower() or selected_character == "1":
    selected_character = punching_baby
    print(f"Woah, you selected {punching_baby.title()}!")
elif selected_character == possessed_bear.lower() or selected_character == "2":
    selected_character = possessed_bear
    print(f"Woah, you selected {possessed_bear.title()}!")
else:
    print(f"Pssst, you didn't select a character. Not putting up with this, buh-BYE.")

# For testing only ===================================

# Attack damage randomizer per character
hit_possessed_bear = random.randint(1, possessed_bear_atk)
hit_punching_baby = random.randint(1, punching_baby_atk)

# Apply attack damage to character's HP
if selected_character == punching_baby:
    update_punching_baby_hp = punching_baby_hp - hit_punching_baby
    print(f"{punching_baby.title()} has been hit with {hit_punching_baby} attack points!")
    print(f"  HP: {update_punching_baby_hp}/{punching_baby_hp}")
    
elif selected_character == possessed_bear:
    update_possessed_bear_hp = possessed_bear_hp - hit_possessed_bear
    print(f"{possessed_bear.title()} has been hit with {hit_possessed_bear} attack points!")
    print(f"  HP: {update_possessed_bear_hp}/{possessed_bear_hp}")

# Counter Attack - Player
# Message for player
print(f"Time for a counter attack {player_name.title()}!")

# Attacking options
print(f"{player_name.title()} select your next move!")
print("> 1. Attack")
print("> 2. Run Away")

next_move = input(f"Please select your next move: ").lower()

while (next_move != "1" and next_move != "attack") and (next_move != "2" and next_move != "run away"):
	next_move = input("Please select a next move: ").lower()

if next_move == "1" or next_move == "attack":
	# REPLACE WITH ATK GEN
	print("TEMP1")
elif next_move == "2" or next_move == "run away":
	# REPLACE WITH POINT DEDUCT GEN
	print("TEMP2")