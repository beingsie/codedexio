# Loot Drop

# Import random module function randint
from random import randint

# Counter trigger for loot drop
trigger_lootdrop = 0

enemy_defeated = True

# DEV
for x in range(0, 35):

    # Trigger a lootdrop after defeating NPC
    if enemy_defeated == True:
        # Lootdrop rarity (0 = no drop, 1-10 = common, 11-15 = rare, 16-18 = epic, 19-20 = legendary)
        trigger_lootdrop = randint(0, 20)

        # Loot rarity
        if trigger_lootdrop >= 1 and trigger_lootdrop <= 10:
            print(f"Common Drop [{trigger_lootdrop}]")
        elif trigger_lootdrop >= 11 and trigger_lootdrop <= 15:
            print(f"Rare Drop [{trigger_lootdrop}]")
        elif trigger_lootdrop >= 16 and trigger_lootdrop <= 18:
            print(f"Epic Drop [{trigger_lootdrop}]")
        elif trigger_lootdrop >= 19 and trigger_lootdrop <= 20:
            print(f"Legendary Drop [{trigger_lootdrop}]")
        else:
            print(f"No luck, empty drop! [{trigger_lootdrop}]")
            