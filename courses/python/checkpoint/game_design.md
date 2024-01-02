# 👨‍💻 Terminal Mini Game
Battle vs NPC's in terminal! Upgrade character through leveling up your `XP`, `HP` and `Attack Power`.
 
## 📃 To-Do:
- [ ] Game Mode Logic
	- [ ] Create a chance based version based on the `randint` function.
- [ ] Character descriptions
- [ ] Game rules
- [ ] FAQs

## ⚡ In Progress:
- [ ] Dice roll
	- [x] Give player a minimum of 1 dice roll.
	- [ ] Auto Selection Countdown (5 seconds: Is enabled if user spends all dice rolls.)
		- **Auto selects** character if player fails to select after using all available dice rolls.

## 🧪 Experimental
### [Battle]
- [ ] `Run Away` - Loses 1/4 of their `XP`.
### [Dialogue]
- [ ] Dialogue using `randint` to pick a line that connects the characters through the `lore` story line. in battle. (After selecting the `run away` option)
### UI
- [ ] Menu selection activate state (Blinking menu cursor).
- [ ] ■■■□□□ bar for `HP`. Calculate the number of empty squares to full depending on their max hp / by 10 (squares)
- [ ] Text-based UI
- [ ] Emojies
- [ ] ANSI escape codes for text colors.
### Gameplay
- [ ] Loot Drops based on item rarity.
- [ ] Dialogue
  - [ ] Back story for each character that connects them via dialogue.
- [ ] Shop
  - User can spend XP for the following items:
	- Heal Packs
	- Upgrades: TEMP
- [ ] Create a testing process similar to Minecraft
  - Commands that alter gameplay:
    - Stats
    - Storyline
- [ ] Story line
  - Chapters
- [ ] Commands
	- [ ] FAQs
	- [ ] Game rules

## ✅ Completed:
### 📅 12/26/23
- [x] Menu Logic [50ea06b](https://github.com/beingsie/codedexio/commit/50ea06b9eb498e8e6fb3908542baa7488bc737ef)
	- [x] Add submenu's
 		- [x] Game Mode: Options `Dice Roll`, `Normal` (Default game mode)
### 📅 11/21/23
- [x] Offensive Attacking. [46809e8](https://github.com/beingsie/codedexio/commit/46809e822fe1c2046c7107ceccf3e47f80655a91)
- [x] Counter Attacking. [46809e8](https://github.com/beingsie/codedexio/commit/46809e822fe1c2046c7107ceccf3e47f80655a91)
### 📅 11/16/23
- [x] Improve character selection input validation with numeration. [632f76f](https://github.com/beingsie/codedexio/commit/632f76f943c0c07c2ffa250061f501e367799c92)
- [x] Create logic to determine the amount of attack power generated for an attack from 'enemies'. [fa3203b](https://github.com/beingsie/codedexio/commit/fa3203b99ab62b6e37504fe2663be78f0fd630d6)
	- Use similar logic from [99 Bottles](https://github.com/beingsie/codedexio/blob/main/courses/python/04_loops/99_bottles.py).
 	- Attack damage range should mirror the up to the character's max damage.

#
#### Hot Fixes:
- `Press Any Key To Continue` option does not work with all keys except `enter`.
