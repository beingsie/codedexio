# UX
# print("""
# ■■■■■■■■■■■□□□
# """)

print("""
░▒▓  PLAYER REGISTRATION  ▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
	  """)

# Player name
player_name = input("     ♢ Enter a Username > ")

# UX
user_secret = input(f"""     ♢ Enter a secret about {player_name.title()} > """)
print("")

input("""     ❖  Press Any Key To Continue  ❖ """)

# Welcome message
print(rf"""
░░░▒▓  ✦ WELCOME TO ✦  ▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      ____  ___    _   ______  __________
     / __ \/   |  / | / / __ \/  _/_  __/
    / /_/ / /| | /  |/ / / / // /  / /   
   / _, _/ ___ |/ /|  / /_/ _/ /  / /    
  /_/ |_/_/ _|_/_/ |_/_____/___/ /_/_____
     / __ \/ __ \ \/ /   |  / /   / ____/
    / /_/ / / / /\  / /| | / /   / __/   
   / _, _/ /_/ / / / ___ |/ /___/ /___   
  /_/ |_|\____/ /_/_/  |_/_____/_____/   
    
     ★ Your secret is safe {player_name.title()}, unless you lose.

░░░░ A terminal game by @Beingsie ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""")

# Main menu
# Intro
input("""     ❖  Press Any Key To Continue  ❖ """)
print("""
╔══════════════════════╗
║     ► Main Menu      ║
╚══════════════════════╝
  ║
  ║ ♢ 1. Start	
  ║ ♢ 2. Game Rules
  ║ ♢ 3. Exit
  ║""")
