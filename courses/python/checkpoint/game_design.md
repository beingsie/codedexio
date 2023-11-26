# 👨‍💻 Terminal Mini Game
Battle vs NPC's in terminal! Upgrade character through leveling up your `XP`, `HP` and `Attack Power`.

## ⚡ In Progress
### UI
- [ ] Text-based UI
- [ ] Emojies
### [Battle]
- [ ] `Run Away` - Loses 1/4 of their `XP`.
### [Dialogue]
- [ ] Dialogue using `randit` to pick a line that connects the characters in battle. (After selecting the `run away` option)
 
## 📃 To-Do:
- [ ] Character descriptions
- [ ] Game rules
- [ ] FAQs

### ⚔ [Battle]

## 🧪 Experimental
- [ ] Dialogue
  - [ ] Back story for each character that connects them via dialogue.
- [ ] Selection Mode
	- Give player ability to select type of character selection mode: `dice roll` or `manual`. 
- [ ] Selection logic based on the `random` module function `randint`.
	- [ ] Dice roll
		- [ ] Give player has 3 dice rolls.
		- [ ] Countdown (5 seconds)
    	- **auto selects** character if player fails to select after using all available dice rolls.
- [ ] Shop
  - User can spend XP for the following items:
	- Heal Packs
	- Upgrades: TEMP
- [ ] Create a testing process similar to Minecraft
  - Commands that alter gameplay:
    - Stats
    - Storyline
- [ ] Add a selection countdown timer
  - Auto selects a character when timer expires.
- [ ] Story line
  - Chapters
- [ ] Commands
	- [ ] FAQs
	- [ ] Game rules

## ✅ Completed:
- [x] Offensive Attacking. [46809e8](https://github.com/beingsie/codedexio/commit/46809e822fe1c2046c7107ceccf3e47f80655a91)
- [x] Counter Attacking. [46809e8](https://github.com/beingsie/codedexio/commit/46809e822fe1c2046c7107ceccf3e47f80655a91)
- [x] Improve character selection input validation with numeration. [632f76f](https://github.com/beingsie/codedexio/commit/632f76f943c0c07c2ffa250061f501e367799c92)
- [x] Create logic to determine the amount of attack power generated for an attack from 'enemies'. [fa3203b](https://github.com/beingsie/codedexio/commit/fa3203b99ab62b6e37504fe2663be78f0fd630d6)
	- Use similar logic from [99 Bottles](https://github.com/beingsie/codedexio/blob/main/courses/python/04_loops/99_bottles.py).
 	- Attack damage range should mirror the up to the character's max damage.
