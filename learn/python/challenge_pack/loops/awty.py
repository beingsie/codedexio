# Initialize answer
answer = 0

# Loop
while answer != "yes":
    # Re-ask user
    answer = input("Are we there yet? ").lower()

    # Exit loop
    if answer == "yes":
        print("Geeze that took so long 😭")