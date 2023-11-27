# Main menu input trigger
main_menu = input("""
MAIN MENU

1. Start
2. Options
3. Exit

""").lower()

# Main menu while loop
while (main_menu != "1" and main_menu != "start") and (main_menu != "2" and main_menu != "options") and (main_menu != "3" and main_menu != "exit"):
	print("Invalid option. Please try again.")

	# Repeat menu if input is invalid
	main_menu = input("""
MAIN MENU

1. Start
2. Options
3. Exit

""").lower()

# START selected
if main_menu == "1" or main_menu == "start":
	start_menu = input("""
START MENU

1. Character Selection
2. Options
3. Back to Main Menu

""").lower()
	
	# START while loop
	while (start_menu != "1" and start_menu != "character selection") and (start_menu != "2" and start_menu != "options") and (start_menu != "3" and start_menu != "back"):
		print("Invalid option. Please try again.")
		start_menu = input("""
START MENU

1. Character Selection
2. Options
3. Back to Main Menu

""").lower()
	if start_menu == "1" or start_menu == "character selection":
		print("[Character selection screen]")
		
	elif start_menu == "2" or start_menu == "options":
		options_menu = input("""
OPTIONS MENU

1. Option1
2. Option2
3. Back to Main Menu

""").lower()
		# OPTIONS while loop
		while (options_menu != "1" and options_menu != "character selection") and (options_menu != "2" and options_menu != "options") and (options_menu != "3" and options_menu != "back"):
			print("Invalid option. Please try again.")
			options_menu = input("""
	OPTIONS MENU
	
	1. Option1
	2. Option2
	3. Back to Main Menu
	
	""").lower()

		if options_menu == "1" or options_menu == "option 1":
			print("Option 1")
		elif options_menu == "2" or options_menu == "option 2":
			print("Option 2")
		else:
			print("Exited back to start menu")
