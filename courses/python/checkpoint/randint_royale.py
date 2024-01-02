# Import randint function from random module
from random import randint

# Menu's are enabled after user successfully registers
user_is_registered = True

# Player name
player_name = input("Enter a Username > ")

# TEMP
# Initialize game mode
game_mode = "normal"

# Characters
char_1 = "char 1"
char_2 = "char 2"
char_3 = "char 3"

# Player selected character
character_selected = 0
character_locked_in = 0

while user_is_registered:
    print("Main Menu")
    print("") # Line space
    print("- Start")
    print("- Game Mode")
    print("- Exit")
    print("") # Line space
    print("Game Mode:", game_mode.title()) # DEBUGGER
    print("") # Line space
    # Selection input
    selection_menu = input(f"{player_name.title()}: ").lower()
    print("") # Line space

    if selection_menu == "start":
        if game_mode == "normal":
            print("Hero Selection")
            print("") # Line space
            print("- Char 1")
            print("") # Line space
            print("- Char 2")
            print("") # Line space
            print("- Char 3")
            print("") # Line space
            print("- Back")
            print("") # Line space

            # Selection input
            selection_menu = input(f"{player_name.title()}: ").lower()
            print("") # Line space

            # Back to main menu
            if selection_menu == "back":
                break
            elif selection_menu == char_1:
                print("Congrats, you have selected", char_1)
                character_selected = char_1
                character_locked_in = True
                break
            elif selection_menu == char_2:
                print("Congrats, you have selected", char_2)
                character_selected = char_2
                character_locked_in = True
                break
            elif selection_menu == char_3:
                print("Congrats, you have selected", char_3)
                character_selected = char_3
                character_locked_in = True
                break
            else:
                print("Please select a character.")
                print("") # Line space

        elif game_mode == "dice roll":
            print("You have 1 dice roll, roll you dice to have it select the character for you!")
            input("Press enter to roll your dice! ")
            print("Dice is rolling ...")

            # Dice Roll: 1-3
            d_roll = randint(1, 3)

            # Automatic character selection
            if d_roll == 1:
                character_selected = char_1
                character_locked_in = True
                print("Dice rolled", char_1)
                break
            elif d_roll == 2:
                character_selected = char_2
                character_locked_in = True
                print("Dice rolled", char_1)
                break
            else:
                character_selected = char_3
                character_locked_in = True
                print("Dice rolled", char_1)
                break

        elif selection_menu == "back":
            # Return to main menu
              break

    elif selection_menu == "game mode":
        # Main menu submenu
        while user_is_registered:
            print("Game Mode")
            print("") # Line space
            print("- Normal")
            print("- Dice Roll")
            print("- Back")
            print("") # Line space
            # Selection input
            selection_menu = input(f"{player_name.title()}: ").lower()

            if selection_menu == "normal":
                game_mode = "normal"
                print("") # Line space
                print("Default mode has been enabled.")
                print("") # Line space
            elif selection_menu == "dice roll":
                game_mode = "dice roll"
                print("") # Line space
                print("Dice Roll has been enabled.")
                print("") # Line space
            elif selection_menu == "back":
                break
            else:
                print("") # Line space
                print("Try again.")
                print("") # Line space

# elif selection_menu == "c":
#     # Main menu submenu
#     while user_is_registered:
#         print("Menu C")
#         print("") # Line space
#         print("- 1")
#         print("- 2")
#         print("- Back")
#         print("") # Line space
#         # Selection input
#         selection_menu = input(f"{player_name.title()}: ").lower()

#         if selection_menu == "back":
#             # Return to main menu
#             break

    elif selection_menu == "exit":
        print("Thanks for playing!")
        break

    else:
        # Return error message if no valid option is selected
        print(f"{player_name.title()}: ")


if character_locked_in == True:
    print("Starting game ...")
