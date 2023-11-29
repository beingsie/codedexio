# Menu's are enabled after user successfully registers
user_is_registered = True

while user_is_registered:
    print("Main Menu")
    print("A")
    print("B")
    print("C")
    # Selection input
    selection_menu = input("Please select an option: ").lower()

    if selection_menu == 'a':
        # Main menu submenu
        while user_is_registered:
            print("Menu A")
            print("1")
            print("2")
            print("Back to main menu")
            # Selection input
            selection_menu = input("Please select an option: ").lower()

            if selection_menu == "back":
                # Return to main menu
                break

    elif selection_menu == 'b':
        # Main menu submenu
        while user_is_registered:
            print("Menu B")
            print("1")
            print("2")
            print("Back to main menu")
            # Selection input
            selection_menu = input("Please select an option: ").lower()

            if selection_menu == "back":
                # Return to main menu
                break

    elif selection_menu == 'c':
        # Main menu submenu
        while user_is_registered:
            print("Menu C")
            print("1")
            print("2")
            print("Back to main menu")
            # Selection input
            selection_menu = input("Please select an option: ").lower()

            if selection_menu == "back":
                # Return to main menu
                break
    else:
        # Return error message if no valid option is selected
        print("No option selected, please try again -")
