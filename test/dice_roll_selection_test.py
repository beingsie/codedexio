from random import randint

print("You have 1 dice roll ...")
input("Press enter to roll your dice! ")
print("Dice is rolling ...")

for x in range(1, 10):
  d_roll = randint(1, 3)
  print(d_roll)
