# Loot Drop

# Import random module function randint
from random import randint

# Counter trigger for loot drop
trigger_lootdrop = 0

enemy_defeated = True

# DEV
for x in range(0, 50):

    # Trigger a lootdrop after defeating NPC
    if enemy_defeated == True:
        # Lootdrop rarity (0 = no drop, 1-4 = common, 5-7 = rare, 8-9 = epic, 10 = legendary)
        trigger_lootdrop = randint(0, 10)

        # Loot rarity
        if trigger_lootdrop in (1, 2, 3, 4):
            print(f"Common Drop [{trigger_lootdrop}]")
        elif trigger_lootdrop in (5, 6, 7):
            print(f"Rare Drop [{trigger_lootdrop}]")
        elif trigger_lootdrop in (8, 9):
            print(f"Epic Drop [{trigger_lootdrop}]")
        elif trigger_lootdrop == 10:
            print(f"Legendary Drop [{trigger_lootdrop}]")
        else:
            print(f"No luck, empty drop! [{trigger_lootdrop}]")
            