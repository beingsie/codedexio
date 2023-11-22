# Import randint function from random module'
from random import randint

# XP reductions for `run away` option
xp = 250

ran_away = int(xp / 4)
ran_away_deduction = xp - ran_away

print(f"You lose {ran_away}XP!")
print(f"Update: {str(ran_away_deduction)}XP")

# Randomized character dialouge
char_dialouge = randint(1, 3)

user_selection = str(input(f"Select 1 or 2: "))

while user_selection != '1' and user_selection != '2':
  user_selection = input(f"Select 1 or 2: ")

if user_selection == '1':
	print(f"PLAYER_ATTACKS_NPC")
else:
	if char_dialouge == 1:
		print(f"NPC_DIALOUGE_1")
	elif char_dialouge == 2:
		print(f"NPC_DIALOUGE_2")
	else:
		print(f"NPC_DIALOUGE_3")
