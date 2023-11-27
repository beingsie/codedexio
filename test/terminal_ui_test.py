# UX
print("""
══ PLAYER REGISTRATION:
	  """)

# Player name
player_name = input("   > Enter a Username: ")

# UX
user_secret = input(f"""   > Enter a secret about {player_name.title()}: """)
print("")

# Welcome message
print(rf"""    Welcome {player_name.capitalize()}, to the Amazing
      ____  ___    _   ______  __________
     / __ \/   |  / | / / __ \/  _/_  __/
    / /_/ / /| | /  |/ / / / // /  / /   
   / _, _/ ___ |/ /|  / /_/ _/ /  / /    
  /_/ |_/_/ _|_/_/ |_/_____/___/ /_/_____
     / __ \/ __ \ \/ /   |  / /   / ____/
    / /_/ / / / /\  / /| | / /   / __/   
   / _, _/ /_/ / / / ___ |/ /___/ /___   
  /_/ |_|\____/ /_/_/  |_/_____/_____/   
    
    > We won't spill your secret.
      Unless you lose.
""")

# Main menu
# Intro
print("""  ║  A terminal game by @Beingsie  ║""")
input("""

     > Press Any Key To Continue
   ═══════════════════════════════""")
print("""
	╔══════════════════════╗
	║     ► Main Menu      ║
	╚══════════════════════╝
  ║
  ║ > 1. Start	
  ║ > 2. Game Rules
  ║ > 3. Exit
  ║""")
 