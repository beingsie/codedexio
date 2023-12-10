# Menu's are enabled after user successfully registers
user_is_registered = True

# Player name
player_name = input("     ♢ Enter a Username > ")

while user_is_registered:
    print("Main Menu")
    print("")
    print("Start")
    print("Options")
    print("Exit")
    print("")
    # Selection input
    print("Select an option")
    selection_menu = input(f"  {player_name.title()}: ").lower()
    print("")

    if selection_menu == "start":
        # Main menu submenu
        while user_is_registered:
            print("Hero Selection")
            print("")
            print("1.) Tracer")
            print("")
            print("--- Also known as Lena Oxton, is a charismatic and agile hero in Overwatch with the unique ability to manipulate time, making her a formidable and beloved member of the game's roster.")
            print("")
            print("2.) Soldier 76")
            print("")
            print("--- Real name is Jack Morrison, is a vigilante-style hero in Overwatch armed with a pulse rifle, tactical visor, and biotic field, known for his relentless pursuit of justice and his iconic mask.")
            print("")
            print("3.) Back")
            print("")

            # Selection input
            selection_menu = input(f"  {player_name.title()}: ").lower()

            if selection_menu == "back":
                # Return to main menu
                break

    elif selection_menu == "b":
        # Main menu submenu
        while user_is_registered:
            print("Menu B")
            print("1")
            print("2")
            print("Back")
            # Selection input
            selection_menu = input(f"  {player_name.title()}: ").lower()

            if selection_menu == "back":
                # Return to main menu
                break

    elif selection_menu == "c":
        # Main menu submenu
        while user_is_registered:
            print("Menu C")
            print("1")
            print("2")
            print("Back")
            # Selection input
            selection_menu = input(f"  {player_name.title()}: ").lower()

            if selection_menu == "back":
                # Return to main menu
                break
    elif selection_menu == "exit":
        print("Thanks for playing!")
        break

    else:
        # Return error message if no valid option is selected
        print(f"  {player_name.title()}: ")
