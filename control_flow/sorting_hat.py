# Harry Potter inspired experience based on The Sorting Hat from the HP Series

# Create Houses
gryffindor_house = "Gryffindor"
ravenclaw_house = "Ravenclaw"
hufflepuff_house = "Hufflepuff"
slytherin_house = "Slytherin"

# UI
# Intro
print('''
🧙: Welcome! I'm the Sorting Hat.
🧙: Lets reveal your true nature.
🧙: I will sort you into one of our four houses.
    
      
🦁 Gryffindor  |  🦡 Hufflepuff  |  🦅 Ravenclaw  |  🐍 Slytherin

      
🧙: Which of these houses calls to you?
      ''')
# Ask for users favored house name
user_house = input('Enter a house name: ')
# Assign favored user house
if user_house == "gryffindor" or user_house == "Gryffindor":
    user_house_name = gryffindor_house
    print('''
🧙: You think you have a courageous heart beats within a Gryffindor?   
🧙: Hmm..
    ''')
elif user_house == "ravenclaw" or user_house == "Ravenclaw":
    print('''
🧙: Do you thirst for knowledge shines brightly like a Ravenclaw? 
🧙: Hmm..
    ''')
    user_house_name = ravenclaw_house
elif user_house == "hufflepuff" or user_house == "Hufflepuff":
    print('''
🧙: Do you believe you radiate kindness and patience like a Hufflepuff?
🧙: Hmm..
    ''')
    user_house_name = hufflepuff_house
elif user_house == "slytherin" or user_house == "Slytherin":
    user_house_name = slytherin_house
    print('''
🧙: Agh, your ambition knows no bounds like a Slytherin, eh?
🧙: Hmm..
    ''')
else:
    # Assign user house as guest house if non of the four houses was chosen
    house_guest = user_house
    print('''
🧙: Ah, an intriguing response, my young ''' + house_guest)
    print('''🧙: However, I must remind you that we are bound by the choices of Gryffindor, Hufflepuff, Ravenclaw, and Slytherin.
    ''')

# Assign favored user house
if user_house == "gryffindor":
    user_house_name = gryffindor_house
    print("🧙: So tell me, my dear " + user_house_name + " as bravery and courage mark your path.")
elif user_house == "ravenclaw":
    user_house_name = ravenclaw_house
    print("🧙: So tell me, my wise " + user_house_name + " as bravery and courage mark your path.")
elif user_house == "hufflepuff":
    user_house_name = hufflepuff_house
    print("🧙: So tell me, my loyal " + user_house_name + " as bravery and courage mark your path.")
elif user_house == "slytherin":
    user_house_name = slytherin_house
    print("🧙: So tell me, my resourceful " + user_house_name + " as bravery and courage mark your path.")

# Create choice question pools
# Question pool 1 [p01]
p01 = '''
🧙: Tell me, do you find yourself more drawn to the embrace of Dawn or the allure of Dusk?
''';
p01_answer_01 = "1.) The fresh start and untamed potential of the morning."
p01_answer_02 = "2.) The warmth and energy of Noon, when the sun shines its brightest."
p01_answer_03 = "3.) The mystical and contemplative moments of Dawn, as the world awakens."
p01_answer_04 = "4.) The intriguing and mysterious atmosphere of Dusk, as night begins to fall."
# Question pool 2 [p02]
p02 = '''
🧙: You want people to remember you as..
'''
p02_answer_01 = "1.) The Good"
p02_answer_02 = "2.) The Great"
p02_answer_03 = "3.) The Wise"
p02_answer_04 = "4.) The Bold"
# Question pool 3 [p03]
p03 = '''
🧙: Which kind of instrument most pleases your ear?
'''
p03_answer_01 = "1.) The violin"
p03_answer_02 = "2.) The trumpet"
p03_answer_03 = "3.) The piano"
p03_answer_04 = "4.) The drum"
# Question pool 4 [p04]
p04 = '''
🧙: In the face of a daunting challenge, which approach resonates with you the most?
'''
p04_answer_01 = "1.) Strategically navigating the challenge, using resourcefulness and cunning to come out on top."
p04_answer_02 = "2.) Rallying a group of friends and working together to overcome the obstacle."
p04_answer_03 = "3.) Analyzing the challenge from all angles and seeking a clever, strategic solution."
p04_answer_04 = "4.) Charging in headfirst with unwavering bravery and determination."

# UI
# Print Question pool 1 as options for the user
print(p01)
print(p01_answer_01)
print(p01_answer_02)
print(p01_answer_03)
print(p01_answer_04)
print()

# User answer
user_answer = int(input("Choose from the options above: "))

# Assign default points to houses
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Reward points to houses
# Question pool 1
if user_answer == 1:
    gryffindor += 10
    print()
    print("🧙: +10 points to " + gryffindor_house + "!")
    print()
elif user_answer == 2:
    hufflepuff += 10
    print()
    print("🧙: +10 points to " + hufflepuff_house + "!")
    print()
elif user_answer == 3:
    ravenclaw += 10
    print()
    print("🧙: +10 points to " + ravenclaw_house + "!")
    print()
elif user_answer == 4:
    slytherin += 10
    print()
    print("🧙: +10 points to " + slytherin_house + "!")
    print()
else:
    print('''
🧙: Ah, an intriguing response, my young ''' + user_house + ". Yet not one of the choices. ")
    print('''🧙: No points awarded!
    ''')
    input("🧙: Press Enter to Continue ")

# UI
# Print Question pool 2 as options for the user

print()
print(p02)
print(p02_answer_01)
print(p02_answer_02)
print(p02_answer_03)
print(p02_answer_04)
print()

# User answer
user_answer = int(input("Choose from the options above: "))
print()

# Reward points to houses
# For question pool 2
if user_answer == 1:
    hufflepuff += 10
    print()
    print("🧙: +10 points to " + hufflepuff_house + "!")
    print()
elif user_answer == 2:
    slytherin += 10
    print()
    print("🧙: +10 points to " + slytherin_house + "!")
    print()
elif user_answer == 3:
    ravenclaw += 10
    print()
    print("🧙: +10 points to " + ravenclaw_house + "!")
    print()
elif user_answer == 4:
    gryffindor += 10
    print()
    print("🧙: +10 points to " + gryffindor_house + "!")
    print()
else:
    print('''
🧙: Ah, an intriguing response, my young ''' + user_house + ". Yet not one of the choices. ")
    print('''🧙: No points awarded!
    ''')
    input("🧙: Press Enter to Continue ")

# UI
# Print Question pool 3 as options for the user
print(p03)
print(p03_answer_01)
print(p03_answer_02)
print(p03_answer_03)
print(p03_answer_04)
print()

# User answer
user_answer = int(input("Choose from the options above: "))

# Reward points to houses
# For question pool 3
if user_answer == 1:
    slytherin += 10
    print()
    print("+10 points to: " + slytherin_house)
elif user_answer == 2:
    hufflepuff += 10
    print()
    print("+10 points to: " + hufflepuff_house)
elif user_answer == 3:
    ravenclaw += 10
    print()
    print("+10 points to: " + ravenclaw_house)
elif user_answer == 4:
    gryffindor += 10
    print()
    print("+10 points to: " + gryffindor_house)
else:
    print('''
🧙: Ah, an intriguing response, my young ''' + user_house + ". Yet not one of the choices. ")
    print('''🧙: No points awarded!
    ''')
    input("🧙: Press Enter to Continue ")

# UI
# Print Question pool 4 as options for the user
print(p04)
print(p04_answer_01)
print(p04_answer_02)
print(p04_answer_03)
print(p04_answer_04)
print()

# User answer
user_answer = int(input("Choose from the options above: "))

# Reward points to houses
# For question pool 4
if user_answer == 1:
    slytherin += 10
    print()
    print("+10 points to: " + slytherin_house)
elif user_answer == 2:
    hufflepuff += 10
    print()
    print("+10 points to: " + hufflepuff_house)
elif user_answer == 3:
    ravenclaw += 10
    print()
    print("+10 points to: " + ravenclaw_house)
elif user_answer == 4:
    gryffindor += 10
    print()
    print("+10 points to: " + gryffindor_house)
else:
    print('''
🧙: Ah, an intriguing response, my young ''' + user_house + ". Yet not one of the choices. ")
    print('''🧙: No points awarded!
    ''')
    input("🧙: Press Enter to Continue ")

# Print updated points for houses
print('''
House points:
''')
print("🦁 " + gryffindor_house + ": " + str(gryffindor) + " points")
print("🦡 " + hufflepuff_house + ": " + str(hufflepuff) + " points")
print("🦅 " + ravenclaw_house + ": " + str(ravenclaw) + " points")
print("🐍 " + slytherin_house + ": " + str(slytherin) + " points")
print()

# Decide wether user favored their correct house
# If all chances missed assign Slytherin
if gryffindor + hufflepuff + ravenclaw + slytherin == 0:
    print('''
🧙: Ah, it seems that our charming owl might have decided to take an extended vacation with your acceptance letter!
🧙: A bit of resourcefulness and ambition, perhaps..
🧙: Ah, an ambitious and resourceful SLYTHERIN!
    ''')
# Assign Gryffindor
elif gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin:
    print('''
🧙: Ah, a true GRYFFINDOR!
🧙: Your courage and determination shine brightly. Welcome to Gryffindor, where you'll find fellow brave souls to embark on daring adventures with. Wear your lion emblem with pride, and let your spirit guide you to greatness!
    ''')
# Assign Hufflepuff
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print('''
🧙: Ah, a loyal HUFFLEPUFF!
🧙: The kindest and most dedicated of hearts. Welcome to your home in Hufflepuff, where you'll find friendships that last a lifetime and a place to channel your unwavering loyalty. The badger shall be your symbol, standing for your resilience and hard work!
    ''')
# Assign Ravenclaw
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print('''
🧙: Ah, a knowledge and wisdom seeking RAVENCLAW!
🧙: The kindest and most dedicated of hearts. Welcome to your home in Hufflepuff, where you'll find friendships that last a lifetime and a place to channel your unwavering loyalty. The badger shall be your symbol, standing for your resilience and hard work!
    ''')
elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
    print('''
🧙: Ah, ambitious and resourceful SLYTHERIN!
🧙: Welcome to your house of cunning and determination. The serpent is your emblem, symbolizing your shrewdness and drive.
🧙: In Slytherin, you'll find a community that values your potential for greatness and the paths you forge.
    ''')
else:
    print('''
🧙: Ahh, a delightful dilemma!
🧙: It seems your heart shares its affections with multiple houses, each offering its own unique charm. Remember, within the walls of Hogwarts, your qualities will flourish regardless of which house you join.
    ''')

# Thanks for playing
print('''
✨ Thanks for playing! ✨
      
🔍 Checkout the GitHub
      - https://github.com/beingsie/codedexio
⭐️ Codedex.io experience documented on Twitter @Beingise
      - https://twitter.com/Beingsie
    ''')