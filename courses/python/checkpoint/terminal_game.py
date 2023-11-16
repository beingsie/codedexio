# Import Random Module
import random

# Characters
possessed_bear = 'possessed bear' # Temp name
punching_baby = 'punching baby' # Temp name

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
player_name = input('Enter your player name: ')
print('')

# Welcome message
print(f'Welcome to Monster Royale {player_name.capitalize()}!')

# - Character Selection
# Display list of characters
print(f'''
[Characters]

> {possessed_bear.title()}
 - HP: {possessed_bear_hp}
 - Attack Power: {possessed_bear_atk}
 
> {punching_baby.title()}
 - HP {punching_baby_hp}
 - Attack Power: {punching_baby_atk}
''')

# Character Selection
selected_character = input('Choose a character: ').lower()

# Repeat asking user to select and available character
while (selected_character != punching_baby and selected_character != '1') and (selected_character != possessed_bear and selected_character != '2'):
  selected_character = input('Please select an available character: ').lower()

if selected_character == punching_baby.lower() or selected_character == '1':
	print(f'Woah, you selected {punching_baby}!')
elif selected_character == possessed_bear.lower() or selected_character == '2':
	print(f'Woah, you selected {possessed_bear}!')
else:
	print(f'Pssst, you didn\'t select a character. Not putting up with this, buh-BYE.')

# For testing only ===================================

# Attack damage randomizer per character
hit_possessed_bear = random.randint(1, possessed_bear_atk)
hit_punching_baby = random.randint(1, punching_baby_atk)

# Apply attack damage to character's HP
update_possessed_bear_hp = possessed_bear_hp - hit_possessed_bear
update_punching_baby_hp = punching_baby_hp - hit_punching_baby

# Outcome per character
# Possessed Bear
print(f'''{possessed_bear.title()} has been hit with {hit_possessed_bear} attack points!''')
print(f'''HP: {update_possessed_bear_hp}/{possessed_bear_hp}''')
print('') # Empty string line
# Punching Baby
print(f'''{punching_baby.title()} has been hit with {hit_punching_baby} attack points!''')
print(f'''HP: {update_punching_baby_hp}/{punching_baby_hp}''')
