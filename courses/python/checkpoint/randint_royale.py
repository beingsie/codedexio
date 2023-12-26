# Menu's are enabled after user successfully registers
user_is_registered = True

# Player name
player_name = input("Enter a Username > ")

while user_is_registered:
    print("Main Menu")
    print("")
    print("- Start")
    print("- Game Mode")
    print("- Exit")
    print("")
    # Selection input
    selection_menu = input(f"{player_name.title()}: ").lower()
    print("")

    if selection_menu == "start":
        # Main menu submenu
        while user_is_registered:
            print("Hero Selection")
            print("")
            print("- Char 1")
            print("")
            print("- Char 2")
            print("")
            print("- Char 3")
            print("")
            print("- Back")
            print("")

            # Selection input
            selection_menu = input(f"{player_name.title()}: ").lower()

            if selection_menu == "back":
                # Return to main menu
                break

    elif selection_menu == "game mode":
        # Main menu submenu
        while user_is_registered:
            print("Game Mode")
            print("")
            print("- Dice Roll")
            print("- Normal")
            print("- Back")
            print("")
            # Selection input
            selection_menu = input(f"{player_name.title()}: ").lower()

            if selection_menu == "dice roll":
                print("Game Mode is now in Dice Roll")
            elif selection_menu == "back":
                break
            else:
                print("Try again.")

    # elif selection_menu == "c":
    #     # Main menu submenu
    #     while user_is_registered:
    #         print("Menu C")
    #         print("")
    #         print("- 1")
    #         print("- 2")
    #         print("- Back")
    #         print("")
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
