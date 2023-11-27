# Import randint function from random module'
from random import randint

# XP reductions for `run away` option
xp = 250

run_away = int(xp / 4)
run_away_deduction = xp - run_away

print(f"You lose {run_away}XP!")
print(f"Update: {str(run_away_deduction)}XP")

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

# Main menu
# Intro
input(f"    > Press Any Key To Continue ")  # Empty Input for interactivity
print("""  ║
╔══════════════════════╗
║     ► Main Menu      ║
╚══════════════════════╝
  ║
    > 1. Start	
    > 2. Game Rules
    > 3. Exit
  ║""")

active_main_menu = str(input("    > Select a menu option: ").lower())
print("  ║")	

while active_main_menu not in ("1", "2", "3") and (active_main_menu not in ("start", "game rules", "exit")):
	active_main_menu = str(input(f"    > Select a menu option: ").lower())
	
if active_main_menu in ("1", "2", "3") or (active_main_menu in ("start", "game rules", "exit")):
	print("  ║")
	print("    > Success")