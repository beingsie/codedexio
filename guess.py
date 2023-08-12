# Correct answer
top_pl_player = "haaland"
# Max chances
max_tries = 9

while True:
    # Ask user for answer
    user_input = input("Who is the top Premiere League player this season? ")
    if user_input != top_pl_player:
        print("Incorrect!")
        max_tries -= 1
        print(str(max_tries) + " tries remaining!")

        if max_tries == 0:
            print("GAME OVER!")
            break
        
    else:
        print("Correct! It's Man City's Erling Haaland, #9!")
        break