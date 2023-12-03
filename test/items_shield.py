# Items: Shield

# Import random module function randint
from random import randint

# Character hp
hp = 150

# Shield points rarity
shield_common = 15
shield_rare = 25
shield_epic = 50
shield_legendary = 75

for x in range(35):

    # Lootdrop rarity generator
    trigger_lootdrop = randint(0, 20)

    # Loot rarity
    if trigger_lootdrop >= 1 and trigger_lootdrop <= 10:
        # Add shield boost to current hp
        hp_shielded = hp + shield_common
        print(hp_shielded)

    elif trigger_lootdrop >= 11 and trigger_lootdrop <= 15:
        # Add shield boost to current hp
        hp_shielded = hp + shield_rare
        print(hp_shielded)

    elif trigger_lootdrop >= 16 and trigger_lootdrop <= 18:
        # Add shield boost to current hp
        hp_shielded = hp + shield_epic
        print(hp_shielded)

    elif trigger_lootdrop >= 19 and trigger_lootdrop <= 20:
        # Add shield boost to current hp
        hp_shielded = hp + shield_legendary
        print(hp_shielded)

    else:
        print(f"No luck, empty drop! [{trigger_lootdrop}]")