
# Emotion score list
emotion_score = [999, 899, 799, 699, 599, 499, 399, 299, 199]

# Emotion list
emotions = {
    "happy": emotion_score[0],
    "excited": emotion_score[1],
    "playful": emotion_score[2],
    "proud": emotion_score[3],
    "calm": emotion_score[4],
    "sleepy": emotion_score[5],
    "sad": emotion_score[6],
    "scared": emotion_score[7],
    "angry": emotion_score[8],
}

# Error default message
error_input = "Error, input not recognized."

# user_state function
def user_e_state():
    while True:
        try:
            # Ask user for emotional state
            user_state = int(input("Emotional state: "))
        
            # Check if input is within valid range
            if user_state in range(1, 10):
                # Get corresponding emotion score
                emotion = emotions[list(emotions.keys())[user_state - 1]]
                print(emotion)
                break
            else:
                # Print error message
                print(error_input)
        except ValueError:
            # Print error message for non-integer input
            print(error_input)

# Call the user_state function
user_e_state()