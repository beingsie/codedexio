# Items: Shield

# Import random module function randint
from random import randint

# Text color & reset
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[36m"
MAGENTA = "\033[95m"
MUSTARD_YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"  # Reset text color to default

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
        hp_shielded = hp + shield_uncommon
        print(f"Lootdrop gave {GRAY}Uncommon Shield{RESET}!")
        print(f"{GREEN}Gained +{shield_uncommon}HP{RESET}")
        print(f"{hp}/{hp_shielded}")
        print()

    elif trigger_lootdrop >= 11 and trigger_lootdrop <= 15:
        # Add shield boost to current hp
        hp_shielded = hp + shield_rare
        print(f"Lootdrop gave {MAGENTA}Rare Shield{RESET}!")
        print(f"{GREEN}Gained +{shield_rare}HP{RESET}")
        print(f"{hp}/{hp_shielded}")
        print()

    elif trigger_lootdrop >= 16 and trigger_lootdrop <= 18:
        # Add shield boost to current hp
        hp_shielded = hp + shield_epic
        print(f"Lootdrop gave {CYAN}Epic Shield{RESET}!")
        print(f"{GREEN}Gained +{shield_epic}HP{RESET}")
        print(f"{hp}/{hp_shielded}")
        print()

    elif trigger_lootdrop >= 19 and trigger_lootdrop <= 20:
        # Add shield boost to current hp
        hp_shielded = hp + shield_legendary
        print(f"Lootdrop gave {MUSTARD_YELLOW}Legendary Shield{RESET}!")
        print(f"{GREEN}Gained +{shield_legendary}HP{RESET}")
        print(f"{hp}/{hp_shielded}")
        print()

    else:
        print(f"No luck, empty drop! [{trigger_lootdrop}]")