# Characters
possessed_bear = 'Possessed Bear' # Temp name
punching_baby = 'Punching Baby' # Temp name

# Universal Stats
xp = 0

# - Character Stats
# Possessed Bear
possessed_bear_hp = 250
possessed_bear_atk = 3

# Punching Baby
punching_baby_hp = 90
punching_baby_atk = 15

# For testing only ===================================

# Player name
player_name = input('Enter your player name: ')
print('')

# Welcome message
print(f'Welcome to Monster Royale {player_name.capitalize()}!')

# - Character Selection
# Display list of characters
print(f'''
[Characters]

> {possessed_bear}
 - HP: {possessed_bear_hp}
 - Attack Power: {possessed_bear_atk}
 
> {punching_baby}
 - HP {punching_baby_hp}
 - Attack Power: {punching_baby_atk}
''')

# Character Selection
selected_character = input('Choose a character: ').lower()

if selected_character == punching_baby.lower():
	print(f'Woah, you selected {punching_baby}!')
elif selected_character == possessed_bear.lower():
	print(f'Woah, you selected {possessed_bear}!')
else:
	print(f'Pssst, you didn\'t select a character. Not putting up with this, buh-BYE.')
