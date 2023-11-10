# Ask user for restaurant rating
user_rating = int(input("Rate the last restaurant you visited (1 out of 5): "))

# Display users rating
if user_rating > 4:
    print("Extraordinary! ⭐️ ⭐️ ⭐️ ⭐️ ⭐️")
elif user_rating >= 4:
    print("Excellent! ⭐️ ⭐️ ⭐️ ⭐️")
elif user_rating >= 3:
    print("Good! ⭐️ ⭐️ ⭐️")
elif user_rating >= 2:
    print("Fair. ⭐️ ⭐️")
else:
    print("Poor.. ⭐️")